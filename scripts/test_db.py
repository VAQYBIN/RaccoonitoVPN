import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import asyncio
from db import get_session
from sqlalchemy import text


async def test_connection():
    async for session in get_session():
        result = await session.execute(text("SELECT 1"))
        print("DB Connection OK:", result.scalar())

if __name__ == "__main__":
    asyncio.run(test_connection())