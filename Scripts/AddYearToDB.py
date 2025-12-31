import sqlite3, sys

year = int(sys.argv[1])

connection = sqlite3.connect('..\\src\\Michigan_Analytics.db')

def main():
    counties = getCounties()

    addCounties(counties)

    print(f"Added {year} to database.")


def getCounties() -> list:
    cursor = connection.cursor()

    query = 'SELECT DISTINCT name FROM counties;'

    queryOutput = cursor.execute(query).fetchall()

    cursor.close()

    return [(q[0], year, q[0], year) for q in queryOutput]

def addCounties(counties):
    cursor = connection.cursor()

    query = """
    INSERT INTO counties (name, year)
    SELECT ?, ?
    WHERE NOT EXISTS (
        SELECT 1 FROM counties WHERE name = ? AND year = ?
    );
    """

    cursor.executemany(query, counties)

    cursor.close()

if __name__ == "__main__": 
    main()

    connection.commit()

    connection.close()