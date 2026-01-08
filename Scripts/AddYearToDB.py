import sqlite3, sys

years = [1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008]

yearsIter = iter(years)

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
    for x in range(len(years)):
        year = next(yearsIter)
        main()

    connection.commit()

    connection.close()