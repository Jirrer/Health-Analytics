import ast
import matplotlib.pyplot as plt

with open('..\\.txt\\Calculations.txt', 'r', newline='') as file:
    Selected_Calculations = [f.replace('\n','').replace('\r','') for f in file]

def getGiniCoeffient(dataInput: str):
    data = ast.literal_eval(dataInput)

    lorenze = calculateLorenze(data)
    showLorenze(lorenze)

    giniCoeffient = calculateGiniCoeffient(lorenze)

    # year = input("Enter the year: ")

    # print('Calculations Output')

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
    return 0.0


def calculateLorenze(data):
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


if __name__ == "__main__":
    for fileName in Selected_Calculations:
        print(f"\tStarting Calculation {fileName}")
        userInput = input("\tEnter needed data: ")
        print(f"\n\t\tCalculation finished - {globals()[fileName](userInput)}")