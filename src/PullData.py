import json
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

    return (True, {'Deaths': deathsCounties, 'Births': birthsCounties})

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