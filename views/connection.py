import asyncpg
from password import get_password

async def get_conn():
    conn = await asyncpg.connect(f'postgres://postgres:{get_password()}@localhost/faculdade_cursos')
    return conn
