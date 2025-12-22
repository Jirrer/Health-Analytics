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