from Methods import getHtmlPage, getCensusCountyIncome, balanceList

Scrap_Dict = {'HealthRank': 'https://www.countyhealthrankings.org/health-data/michigan?year=2023&tab=1'

}

with open('..\\.txt\\ScrapeData.txt', 'r', newline='') as file:
    Selected_Scraps = [f.replace('\n','').replace('\r','') for f in file]

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
    for fileName in Selected_Scraps:
        print(f"Starting scrap {fileName}")
        userInput = input("Enter needed data: ")
        print(f"Scrap finished - {globals()[fileName](userInput)}")