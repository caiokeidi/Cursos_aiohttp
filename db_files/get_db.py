import asyncpg
from .connection import get_conn

async def get_cursos_db():
    conn = await get_conn()
    infos = await conn.fetch('SELECT * FROM CURSOS')
    await conn.close()
    return infos