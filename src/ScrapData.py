from Methods import getHtmlPage

Scrap_Dict = {'HealthRank': 'https://www.countyhealthrankings.org/health-data/michigan?year=2023&tab=1'

}

with open('.txt\\ScrapData.txt', 'r', newline='') as file:
    Selected_Scraps = [f.replace('\n','').replace('\r','') for f in file]

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
        print(f"\tStarting scrap {fileName}")
        print(f"\t\tScrap finished - {globals()[fileName]()}")