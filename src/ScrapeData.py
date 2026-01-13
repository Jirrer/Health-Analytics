import sys
from typing import get_type_hints
from src.Methods import getHtmlPage, getCensusCountyIncome, balanceList

Scrap_Dict = {'HealthRank': 'https://www.countyhealthrankings.org/health-data/michigan?year=2023&tab=1',
              'DeathNumbers': 'Data\\Deaths.txt',
            }

def getDeaths() -> dict:
    # To-Do: need to clean up data before proessing

    output = {}

    with open(Scrap_Dict['DeathNumbers']) as file:
        pageContent = file.read()

    pageRows = pageContent.split("\n")

    years = [y for y in pageRows[0].split()[1:]]

    for row in pageRows[2:]:
        rowContent = row.split()
        
        if not rowContent: continue

        output[rowContent[0]] = []

        for index in range(1, len(rowContent)): 
            output[rowContent[0]].append((years[index - 1], rowContent[index]))

    return output

def getBirths() -> list:
    pass


def unenploymentPercentage(year: int) -> dict:
    output = {}



    return output

def lorenzeInfo(year: int) -> dict: # PLEASE REFACTOR
    output = {}

    incomeRanges = [5000, 12500, 20000, 30000, 42500, 62500, 87500, 125000, 175000, 250000]

    censusOutcome = getCensusCountyIncome(year)

    if int(year) > 2010:
        countNameIndex = 1
        populationIndex = 2
        brackets = [6, 10, 14, 18, 22, 26, 30, 34, 38, 42]

    else:
        countNameIndex = 129
        populationIndex = 1
        brackets = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

    for countyInfo in censusOutcome[1:]:
        countyName = countyInfo[countNameIndex]

        population = float(countyInfo[populationIndex])

        rawBrackets = [(float(countyInfo[brackets[index]]) * 0.01) * population for index in range(len(brackets))]

        bracketsIncome = [(rawBrackets[i] * incomeRanges[i]) for i in range(len(brackets))]

        balancedBuckets = balanceList(population, rawBrackets)

        bracketsOutput = [(incomeRanges[i], balancedBuckets[i]) for i in range(len(brackets))]

        totalIncome = sum(bracketsIncome)

        output[(countyName[:-10], year)] = [
            (int(population), int(totalIncome)),
            *bracketsOutput
        ]

    return output

def medianIncome():
    pass

def healthRank():
    # Need - county name, year, rank
    soup = getHtmlPage(Scrap_Dict['HealthRank'])

    # healthRankTable = soup.find("table", {"id": "state-snapshot-data-table"})

    tables = soup.find_all("table")

    print(tables)

    # trs = healthRankTable.find_all('tr')
    # for row in trs:
    #     cells = row.find_all(["td", "th"])  # td = data, th = header
    #     cell_texts = [cell.get_text(strip=True) for cell in cells]
    #     print(cell_texts)

if __name__ == "__main__":
    print("Starting ScrapeDat.py")

    selectedScrapes = [s for s in sys.argv[1:]]

    for scrape in selectedScrapes:
        print(f'Starting Calculation {scrape}')

        try:
            func = globals()[scrape]  
        except KeyError:
            print(f"Calculation '{scrape}' not found")
            continue  

        try:
            neededInfo = get_type_hints(func)

            givenInfo = []

            for var, hint in neededInfo.items():
                givenInfo.append(input(f'Enter data for {var} ({hint.__name__}): '))
            
            func(*givenInfo)

        except Exception as e:
            print(f"An error occurred while running '{scrape}': {e}")

        print(f'Ended Calculation {scrape}')

    print("Ended CalculateData.py")