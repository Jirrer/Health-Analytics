import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from datetime import datetime
import src.database


def getCurrentYear() -> int:
    return datetime.now().year

def balanceList(dataTotal: int, unbalencedList: list) -> list:
    output = []
    running = 0

    for i in range(9):
        v = round(unbalencedList[i])
        output.append(v)
        running += v

    output.append(int(dataTotal - running))

    return output

def showLorenze(lorenzePoints):
    x = [p[0] for p in lorenzePoints]
    y = [p[1] for p in lorenzePoints]

    plt.plot(x, y, drawstyle='steps-post', label='Lorenz Curve', color='blue')

    plt.plot([0,1], [0,1], linestyle='--', color='red', label='Line of Equality')

    plt.xlabel('Cumulative Share of Households')
    plt.ylabel('Cumulative Share of Income')
    plt.title('Lorenz Curve')
    plt.legend()
    plt.grid(True)
    plt.show()

def pushCalculations(results: list, query: str):
    queryStatus, queryOutcome = src.database.makeManyQuery(query, results)

    if not queryStatus:
        print(f'Error adding to databsae - {queryOutcome}')

def prepareCountyName(oldName: str):
    return oldName.replace('.', '_').replace(' ','')

def getCensusCountyIncome(year: int):
    url = f"https://api.census.gov/data/{year}/acs/acs5/subject?get=group(S1901)&ucgid=pseudo(0400000US26$0500000)"

    response = requests.get(url)
    
    return response.json()
    
def groupByCounty(data: list) -> dict: # refactor
    output = {}

    counties = [i[0] for i in data]

    for county in counties:
        if county not in output:
            output[county] = []
    
    for value in data:
        index = 1
        currOutput = []

        while (index < len(value)):
            currOutput.append(value[index])

            index += 1

        output[value[0]].append(tuple(currOutput))

    return output

def getHtmlPage(url: str) -> BeautifulSoup:
    response = requests.get(url)
    
    pageContent = response.text

    return BeautifulSoup(pageContent, 'html.parser')