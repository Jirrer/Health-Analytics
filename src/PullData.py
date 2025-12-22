import json
from src.Methods import makeSingleQuery

def pullMedianIncome() -> tuple[bool, dict]:
    query = "SELECT name, year, Median_Income FROM counties ORDER BY name, year"

    queryStatus, queryResponse = makeSingleQuery(query)

    if not queryStatus: 
        return (False, queryResponse)

    groupedCounties = groupByCounty(queryResponse)

    return (True, groupedCounties)


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