from Methods import getHtmlPage

Scrap_Dict = {'HealthRank': 'https://www.countyhealthrankings.org/health-data/michigan?year=2023&tab=1'

}

with open('..\\.txt\\ScrapeData.txt', 'r', newline='') as file:
    Selected_Scraps = [f.replace('\n','').replace('\r','') for f in file]


# Total	33995
#     Less than $10,000	4.6
#     $10,000 to $14,999	2.5
#     $15,000 to $24,999	7.1
#     $25,000 to $34,999	7.2
#     $35,000 to $49,999	15.5
#     $50,000 to $74,999	16.8
#     $75,000 to $99,999	12.3
#     $100,000 to $149,999	22.2
#     $150,000 to $199,999	6.4
#     $200,000 or more	5.4

# data = [
#     (5000,   1564),   # < $10,000
#     (12500,   850),   # $10k–14,999
#     (20000,  2414),   # $15k–24,999
#     (30000,  2448),   # $25k–34,999
#     (42500,  5269),   # $35k–49,999
#     (62500,  5711),   # $50k–74,999
#     (87500,  4181),   # $75k–99,999
#     (125000, 7547),   # $100k–149,999
#     (175000, 2176),   # $150k–199,999
#     (250000, 1836)    # $200k+ (assumed)
# ]

def lorenzeInfo():
    

    return [
    (33995, 2870947500),
    (5000,   1564),
    (12500,   850), 
    (20000,  2414), 
    (30000,  2448), 
    (42500,  5269),   
    (62500,  5711),   
    (87500,  4181),   
    (125000, 7547),  
    (175000, 2176),   
    (250000, 1836)   
]




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