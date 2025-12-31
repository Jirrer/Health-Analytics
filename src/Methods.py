import sqlite3, requests
from bs4 import BeautifulSoup

Database_Connection = 'Michigan_Analytics.db'

def getCensusCountyIncome(year: int):
    url = f"https://api.census.gov/data/{year}/acs/acs5/subject?get=group(S1901)&ucgid=pseudo(0400000US26$0500000)"

    response = requests.get(url)
    
    return response.json()

def makeSingleQuery(query, params=None) -> tuple[bool, list] | tuple[bool, None]:
    try:
        connection = sqlite3.connect(Database_Connection)
        cursor = connection.cursor()

        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        connection.commit()

        if query.strip().lower().startswith("select"):
            results = cursor.fetchall()
        else:
            results = cursor.rowcount

        cursor.close()
        connection.close()
        return (True, results)

    except sqlite3.OperationalError as e:
        return (False, f"Error executing query - {str(e)}")
    except Exception as e:
        return (False, str(e))
    
def makeManyQuery(query, data) -> tuple[bool, int] | tuple[bool, str]:
    try:
        connection = sqlite3.connect(Database_Connection)
        cursor = connection.cursor()

        cursor.executemany(query, data)
        connection.commit()

        affected_rows = cursor.rowcount

        cursor.close()
        connection.close()

        return (True, affected_rows)

    except sqlite3.OperationalError as e:
        return (False, f"Error many querying the database - {str(e)}")

    except Exception as e:
        return (False, str(e))
    
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

def getHtmlPage(url: str) -> BeautifulSoup:
    response = requests.get(url)
    
    pageContent = response.text

    return BeautifulSoup(pageContent, 'html.parser')