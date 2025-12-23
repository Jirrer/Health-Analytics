import sqlite3

Database_Connection = 'src\\Michigan_Analytics.db'

def makeSingleQuery(query) -> tuple[bool, list] | tuple[bool, None]:
    try:
        with sqlite3.connect(Database_Connection) as connection:    
            cursor = connection.cursor()

            results = cursor.execute(query).fetchall()

            return (True, results)
        
    except sqlite3.OperationalError as e:
        return (False, f"Error querying the database - {str(e)}")
    
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