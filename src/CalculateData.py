import ast
import src.ScrapeData
from src.Methods import prepareCountyName, pushCalculations

with open('.txt\\Calculations.txt', 'r', newline='') as file:
    Selected_Calculations = [f.replace('\n','').replace('\r','') for f in file]

def GiniCoeffient(year: int):
    scrappedData = src.ScrapeData.lorenzeInfo(year)

    counties = []

    for countyInfo, data in scrappedData.items():
        lorenze = calculateLorenze(data)

        giniCoeffient = calculateGiniCoeffient(lorenze)

        counties.append((round(giniCoeffient, 3), prepareCountyName(countyInfo[0][:len(countyInfo[0]) - 7]), countyInfo[1]))

    print('Gini Coeffients')
    for x in counties:
        print(f'\t{x[1]} - {x[0]}')

    pushCalculations(counties, "UPDATE counties SET Gini_Coeffient = ? WHERE name = ? AND year = ?")
            
def calculateLorenze(data) -> list:
    plots = []

    population, totalIncome = data[0]

    x, y = None, None
    for index in range(1, len(data)):
        x_numerator = 0
        for j in range(1, index):
            x_numerator += data[j][1]

        x = x_numerator / population
        
        y_numerator = 0
        for j in range(1, index):
            y_numerator += data[j][1] * data[j][0]
        
        y = y_numerator / totalIncome

        plots.append((x, y))

    plots.append((1.0, 1.0))

    return plots

def calculateGiniCoeffient(lorenze) -> float | int:
    area_B = getLorenzeArea(lorenze)

    return 1 - 2 * area_B

def getLorenzeArea(plots: list) -> int:
    areas = [None] * (len(plots) - 1)

    for index in range(len(plots) - 1):
        x_i, y_i = plots[index]

        x_i_1, y_i_1 = plots[index + 1]

        areas[index] = ((y_i + y_i_1) / 2) * (x_i_1 - x_i) 

    return sum(areas)
    
if __name__ == "__main__":
    for caclulation in Selected_Calculations:
        print(f"Starting Calculation {caclulation}")
        
        try: globals()[caclulation](input("Enter needed info: "))
        
        except Exception as e:
            if e == KeyError: print(f"Calculation '{caclulation}' not found")