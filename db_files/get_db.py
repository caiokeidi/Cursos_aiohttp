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
    await conn.close()
    return curso

async def get_cursos_nome_db(nome):
    conn = await get_conn()
    # cursos = await conn.fetch(f"""SELECT * FROM CURSOS WHERE UPPER(NOME) LIKE UPPER('%{nome}%')""")
    cursos = await conn.fetch(f"""SELECT * FROM CURSOS WHERE to_tsvector(NOME) @@ to_tsquery('{nome}') ORDER BY ID""")
    await conn.close()
    return cursos