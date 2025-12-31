from Methods import getHtmlPage, getCensusCountyIncome

Scrap_Dict = {'HealthRank': 'https://www.countyhealthrankings.org/health-data/michigan?year=2023&tab=1'

}

with open('..\\.txt\\ScrapeData.txt', 'r', newline='') as file:
    Selected_Scraps = [f.replace('\n','').replace('\r','') for f in file]

def lorenzeInfo(year: int) -> dict: # PLEASE REFACTOR

    # change truncante to 
    # balanced = []
    # running = 0

    # for i in range(9):
    #     v = round(rawBrackets[i])
    #     balanced.append(v)
    #     running += v

    # balanced.append(int(population - running))

    if int(year) > 2010:
        countNameIndex = 1
        populationIndex = 2
        bracket1 = 4
        bracket2 = 6
        bracket3 = 8
        bracket4 = 10
        bracket5 = 12
        bracket6 = 14
        bracket7 = 16
        bracket8 = 18
        bracket9 = 20
        bracket10 = 22

    else:
        countNameIndex = 129
        populationIndex = 1
        bracket1 = 3
        bracket2 = 5
        bracket3 = 7
        bracket4 = 9
        bracket5 = 11
        bracket6 = 13
        bracket7 = 15
        bracket8 = 17
        bracket9 = 19
        bracket10 = 21

    output = {}

    censusOutcome = getCensusCountyIncome(year)

    incomeRanges = [5000, 12500, 20000, 30000, 42500, 62500, 87500, 125000, 175000, 250000]

    for countyInfo in censusOutcome[1:]:
        countyName = countyInfo[countNameIndex]
        population = float(countyInfo[populationIndex])

        rawBrackets = [
            (float(countyInfo[bracket1]) * 0.01) * population,
            (float(countyInfo[bracket2]) * 0.01) * population,
            (float(countyInfo[bracket3]) * 0.01) * population,
            (float(countyInfo[bracket4]) * 0.01) * population,
            (float(countyInfo[bracket5]) * 0.01) * population,
            (float(countyInfo[bracket6]) * 0.01) * population,
            (float(countyInfo[bracket7]) * 0.01) * population,
            (float(countyInfo[bracket8]) * 0.01) * population,
            (float(countyInfo[bracket9]) * 0.01) * population,
            (float(countyInfo[bracket10]) * 0.01) * population,
        ]

        bracketsIncome = [(rawBrackets[i] * incomeRanges[i]) for i in range(10)]

        totalIncome = sum(bracketsIncome)

        bracketsOutput = [(incomeRanges[i], int(rawBrackets[i])) for i in range(10)]

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
    for fileName in Selected_Scraps:
        print(f"Starting scrap {fileName}")
        userInput = input("Enter needed data: ")
        print(f"Scrap finished - {globals()[fileName](userInput)}")