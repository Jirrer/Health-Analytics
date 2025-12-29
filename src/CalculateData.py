import ast
import matplotlib.pyplot as plt
import ScrapeData
from Methods import makeManyQuery

# DB only supports up to 2010-2022

with open('..\\.txt\\Calculations.txt', 'r', newline='') as file:
    Selected_Calculations = [f.replace('\n','').replace('\r','') for f in file]

def giniCoeffient():
    scrappedData = ScrapeData.lorenzeInfo()

    counties = []

    for countyInfo, data in scrappedData.items():
        lorenze = calculateLorenze(data)

        giniCoeffient = calculateGiniCoeffient(lorenze)

        counties.append((round(giniCoeffient, 3), countyInfo[0], countyInfo[1]))

    print('Gini Coeffients')
    for x in counties:
        print(f'\t{x[1]} - {x[0]}')

    userInput = input("Push To Database? (Type YES): ")

    if userInput == "YES":
        queryStatus, queryOutcome = makeManyQuery('UPDATE counties SET Gini_Coeffient = ? WHERE name = ? AND year = ?', counties)

        if not queryStatus:
            print(queryOutcome)
            
def calculateLorenze(data):
    print(" * Starting Lorenze Calculation")
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

def showLorenze(lorenzePoints):
    x = [p[0] for p in lorenzePoints]
    y = [p[1] for p in lorenzePoints]

    plt.plot(x, y, drawstyle='steps-post', label='Lorenz Curve', color='blue')

    # Line of equality
    plt.plot([0,1], [0,1], linestyle='--', color='red', label='Line of Equality')

    plt.xlabel('Cumulative Share of Households')
    plt.ylabel('Cumulative Share of Income')
    plt.title('Lorenz Curve')
    plt.legend()
    plt.grid(True)
    plt.show()

def calculateGiniCoeffient(lorenze):
    print(" * Starting Gini Coeffient Calculation")

    area_B = getLorenzeArea(lorenze)

    area_A = 0.5 - area_B

    return 1 - 2 * area_B

def getLorenzeArea(plots: list) -> int:
    areas = [None] * (len(plots) - 1)

    for index in range(len(plots) - 1):
        x_i, y_i = plots[index]

        x_i_1, y_i_1 = plots[index + 1]

        areas[index] = ((y_i + y_i_1) / 2) * (x_i_1 - x_i) 

    return sum(areas)
    
if __name__ == "__main__":
    for fileName in Selected_Calculations:
        print(f"Starting Calculation {fileName}")
        globals()[fileName]()