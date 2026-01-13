import sys
from typing import get_type_hints
from src.Methods import makeSingleQuery, groupByCounty

def pullDeath_Birth(county) -> tuple[bool, dict]: 
    deathsQuery = f"SELECT name, year, Deaths FROM counties WHERE name = '{county}' ORDER BY name, year"

    birthsQuery = f"SELECT name, year, Births FROM counties WHERE name = '{county}' ORDER BY name, year"

    deathsQueryStatus, deathsQueryResponse = makeSingleQuery(deathsQuery)

    birthsQueryStatus, birthsQueryResponse = makeSingleQuery(birthsQuery)

    if not deathsQueryStatus: 
        return (False, deathsQueryResponse)
    
    if not birthsQueryStatus:
        return (False, birthsQueryResponse)

    deathsCounties = groupByCounty(deathsQueryResponse)

    birthsCounties = groupByCounty(birthsQueryResponse)

    return (True, {county: {'Deaths': deathsCounties[county], 'Births': birthsCounties[county]}})

pullDeath_Birth('Clinton')

def pullMedianIncome(county) -> tuple[bool, dict]: 
    query = f"SELECT name, year, Median_Income FROM counties WHERE name = '{county}' ORDER BY name, year"

    queryStatus, queryResponse = makeSingleQuery(query)

    if not queryStatus: 
        return (False, queryResponse)

    groupedCounties = groupByCounty(queryResponse)

    return (True, groupedCounties)

def pullHealthRank(county) -> tuple[bool, dict]:
    query = f"SELECT name, year, health_rank FROM counties WHERE name = '{county}' ORDER BY name, year"

    queryStatus, queryResponse = makeSingleQuery(query)

    if not queryStatus: 
        return (False, queryResponse)

    groupedCounties = groupByCounty(queryResponse)

    return (True, groupedCounties)

def pullGiniCoeffient(county) -> tuple[bool, dict]:
    query = f"SELECT name, year, Gini_Coeffient FROM counties WHERE name = '{county}' ORDER BY name, year"

    queryStatus, queryResponse = makeSingleQuery(query)

    if not queryStatus: 
        return (False, queryResponse)

    groupedCounties = groupByCounty(queryResponse)

    return (True, groupedCounties)

if __name__ == "__main__":
    print("Starting PullData.py")

    selectedPulls = [p for p in sys.argv[1:]]

    for pull in selectedPulls:
        print(f'Starting Pull {pull}')

        try:
            func = globals()[pull]  
        except KeyError:
            print(f"Pull '{pull}' not found")
            continue  

        try:
            neededInfo = get_type_hints(func)

            givenInfo = []

            for var, hint in neededInfo.items():
                givenInfo.append(input(f'Enter data for {var} ({hint.__name__}): '))
            
            func(*givenInfo)

        except Exception as e:
            print(f"An error occurred while running '{pull}': {e}")

        print(f'Ended Pull {pull}')

    print("Ended PullData.py")