#!/usr/bin/env python3
"""
Concurrent Asynchronous Database Queries using aiosqlite
"""

import aiosqlite
import asyncio


DB_PATH = "users.db"  # Ensure this SQLite DB exists with a 'users' table


async def async_fetch_users():
    """Fetch all users from the users table"""
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT * FROM users")
        rows = await cursor.fetchall()
        print("All users:")
        for row in rows:
            print(row)
        await cursor.close()


async def async_fetch_older_users():
    """Fetch users older than 40 from the users table"""
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT * FROM users WHERE age > 40")
        rows = await cursor.fetchall()
        print("\nUsers older than 40:")
        for row in rows:
            print(row)
        await cursor.close()


async def fetch_concurrently():
    """Run both queries concurrently"""
    await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )


if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
