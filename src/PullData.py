import json
from Methods import makeSingleQuery
from Methods import groupByCounty

def pullMedianIncome(county) -> tuple[bool, dict]: #fix slq injection
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