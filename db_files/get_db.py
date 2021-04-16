import asyncpg
from .connection import get_conn

async def get_cursos_db():
    conn = await get_conn()
    infos = await conn.fetch('SELECT * FROM CURSOS')
    await conn.close()
    return infos

async def get_curso_db(id):
    conn = await get_conn()
    curso = await conn.fetch(f'SELECT * FROM CURSOS WHERE ID = {id}')
    return curso