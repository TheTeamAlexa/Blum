import asyncio
import aiosqlite
from pathlib import Path

database = Path(__file__).parent / "database.sqlite3"

async def insert(id, first_name):
    query = """
    INSERT INTO accounts (id, first_name, balance, token, useragent) VALUES (?, ?, ?, ?, ?)
    """
    values = (id, first_name, None, None, None)
    async with aiosqlite.connect(database) as db:
        await db.execute(query, values)
        await db.commit()

async def update_useragent(id, useragent):
    query = """UPDATE accounts SET useragent = ? WHERE id = ?"""
    async with aiosqlite.connect(database) as db:
        await db.execute(query, (useragent, id))
        await db.commit()

async def update_balance(id, balance):
    query = """UPDATE accounts SET balance = ? WHERE id = ?"""
    async with aiosqlite.connect(database) as db:
        await db.execute(query, (balance, id))
        await db.commit()

async def update_token(id, token):
    query = """UPDATE accounts SET token = ? WHERE id = ?"""
    async with aiosqlite.connect(database) as db:
        await db.execute(query, (token, id))
        await db.commit()

async def get_by_id(id):
    query = """SELECT * FROM accounts WHERE id = ?"""
    async with aiosqlite.connect(database) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(query, (id,)) as res:
            result = await res.fetchone()
            return dict(result) if result else None

async def get_all():
    query = """SELECT id, first_name, balance FROM accounts"""
    async with aiosqlite.connect(database) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(query) as res:
            return [dict(row) for row in await res.fetchall()]

async def init():
    async with aiosqlite.connect(database) as db:
        await db.execute("CREATE TABLE IF NOT EXISTS accounts (id INTEGER PRIMARY KEY, first_name TEXT, balance TEXT, token TEXT, useragent TEXT)")
        await db.execute("PRAGMA foreign_keys = true")
        await db.commit()

# Test function for demonstration (comment out in production)
async def test():
    await insert(1, "John Doe")
    await update_balance(1, 1000)
    await update_token(1, "sample_token")
    print(await get_by_id(1))
    print(await get_all())

# Initialize database
asyncio.run(init())
print("Enhanced by TheTeamAlexa")
