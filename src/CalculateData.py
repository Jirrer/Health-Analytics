import ast
from src import ScrapeData
from src.Methods import prepareCountyName, pushCalculations

with open('.txt\\Calculations.txt', 'r', newline='') as file:
    Selected_Calculations = [f.replace('\n','').replace('\r','') for f in file]

CurrentYear = 2025

def Deaths():
    deaths = ScrapeData.getDeaths()

    print('Deaths')
    for name, info in deaths.items():
        print(f'{name} - {info}')

    userInput = input("Push To Database? (Type YES): ")

    if userInput != "YES": return

    for name in deaths.keys():
        databaseList = [(i[1], name, i[0]) for i in deaths[name]]
        
        pushCalculations(databaseList, "UPDATE counties SET Deaths = ? WHERE name = ? AND year = ?")

    print("Added new Deaths to database")

def GiniCoeffient(year: int):
    if year < 2010 or year > CurrentYear: print('Invalid Year'); return -1

    scrappedData = ScrapeData.lorenzeInfo(year)

    counties = []

    for countyInfo, data in scrappedData.items():
        lorenze = calculateLorenzePlots(data)

        giniCoeffient = calculateGiniCoeffient(lorenze)

        counties.append((round(giniCoeffient, 3), prepareCountyName(countyInfo[0][:len(countyInfo[0]) - 7]), countyInfo[1]))

    print('Gini Coeffients')
    for x in counties:
        print(f'\t{x[1]} - {x[0]}')

    userInput = input("Push To Database? (Type YES): ")

    if userInput != "YES": return

    pushCalculations(counties, "UPDATE counties SET Gini_Coeffient = ? WHERE name = ? AND year = ?")
            
def calculateLorenzePlots(data) -> list:
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

def calculateGiniCoeffient(lorenze: list[tuple[float, float]]) -> float:
    area_B = getLorenzeArea(lorenze)

    giniCoeffient = 1 - 2 * area_B

    if giniCoeffient > 0.5 or giniCoeffient < 0.0: raise ValueError("Gini Coeffient must be between 0-0.5")

    return giniCoeffient

def getLorenzeArea(plots: list[tuple[float, float]]) -> float: # Area under the Lorenz Curve
    areas = [None] * (len(plots) - 1)

    if len(areas) <= 1: raise ValueError("Not enough plots provided")

    for index in range(len(plots) - 1):
        x_i, y_i = plots[index]

        x_i_1, y_i_1 = plots[index + 1]

        areas[index] = ((y_i + y_i_1) / 2) * (x_i_1 - x_i) 

    for i in range(1, len(plots)):
        if plots[i][0] < plots[i-1][0]:
            raise ValueError("Plots are not sorted")

    totalArea = sum(areas)

    if totalArea > 1.0 or totalArea < 0.0: raise ValueError("Lorenz Curve must be between 0-1")

    return totalArea
    
if __name__ == "__main__":
    for calculation in Selected_Calculations:
        print(f"Starting Calculation {calculation}")
        
        try:
            func = globals()[calculation]  
        except KeyError:
            print(f"Calculation '{calculation}' not found")
            continue  

        try:
            userInput = input("Enter needed info: ")

            if userInput: func(input("Enter needed info: "))
            else: func()

        except Exception as e:
            print(f"An error occurred while running '{calculation}': {e}")