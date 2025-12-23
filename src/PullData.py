import json
from src.Methods import makeSingleQuery
from src.Methods import groupByCounty

def pullMedianIncome() -> tuple[bool, dict]:
    query = "SELECT name, year, Median_Income FROM counties ORDER BY name, year"

    queryStatus, queryResponse = makeSingleQuery(query)

    if not queryStatus: 
        return (False, queryResponse)

    groupedCounties = groupByCounty(queryResponse)

    return (True, groupedCounties)

def pullHealthRank() -> tuple[bool, dict]:
    query = "SELECT name, year, health_rank FROM counties ORDER BY name, year;"

    queryStatus, queryResponse = makeSingleQuery(query)

    if not queryStatus: 
        return (False, queryResponse)

    groupedCounties = groupByCounty(queryResponse)

    return (True, groupedCounties)