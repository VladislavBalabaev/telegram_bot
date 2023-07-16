import sqlite3 as sq

def sql_start():
    global base, cur
    base = sq.connect('drom.db')    # creates a file if there isn't one
    cur = base.cursor()
    if base:
        print('Connection to database is set.')
    base.execute("""
    CREATE TABLE IF NOT EXISTS ads_of_cars(
        brand TEXT, model TEXT, id_of_ad INT PRIMARY KEY, price INT
    )
                """)
    base.commit()

async def sql_add_commit(state):
    async with state.proxy() as data:
        cur.execute("""INSERT INTO ads_of_cars VALUES (?, ?, ?, ?)""", tuple(data.values()))
        base.commit()

async def sql_read():
    return len(cur.execute("""SELECT COUNT(*) FROM ads_of_cars""").fetchall())
