import sys, os, csv, sqlite3

MedianIncomeLocation, HealthRankLocation = None, None

def main():
    medianIncome, healthRank = getData(MedianIncomeLocation), getData(HealthRankLocation)
    
    totalData = getTotalData(medianIncome, healthRank)

    finalData = getFinalData(totalData)

    pushData(finalData)
    
def getData(filesLocation):
    output = []

    fileLocations = [file for file in os.listdir(filesLocation)]

    for fileName in fileLocations:
        countyName = fileName[:len(fileName) - 4]
        
        with open(f"{filesLocation}\\{fileName}", 'r', newline='') as file:
            reader = csv.reader(file)

            next(reader)

            for row in reader:
                output.append([countyName, row[0].replace(' ', '').replace('\t',''), row[1]])

    return output

def getTotalData(income, rank):
    incomeDict, rankDict = getDict(income), getDict(rank)

    output = {}

    for key, value in incomeDict.items():
        if key not in output:
            output[key] = [value, None]

    for key, value in rankDict.items():
        if key in output:
            output[key][1] = value
        
        else:
            output[key] = ['', value]

    return output

    
def getDict(lst):
    output = {}

    for data in lst:
        name, year = data[0], int(data[1])

        if (name, year) not in output:
            output[(name, year)] = data[2]

    return output

def getFinalData(dct):
    output = []

    for key, value in dct.items():
        name, year = key[0], key[1]
        income, rank = value[0], value[1]

        output.append((name, year, income, rank))

    return output

def pushData(lst):
    connection = sqlite3.connect('src\\Michigan_Analytics.db')
    cursor = connection.cursor()

    query = "INSERT INTO counties (name, year, median_income, health_rank) VALUES (?, ?, ?, ?)"

    cursor.executemany(query, lst)

    connection.commit()

    connection.close()

if __name__ == "__main__":
    MedianIncomeLocation = sys.argv[1]
    HealthRankLocation = sys.argv[2]
    main()