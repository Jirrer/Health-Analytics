from dotenv import load_dotenv
import os, sqlite3

load_dotenv()

Database_Connection = os.getenv('DATABASE')

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