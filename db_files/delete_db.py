from .connection import get_conn

async def deleta_curso_db(id):
    conn = await get_conn()
    delete_info = await conn.execute(f'DELETE FROM CURSOS WHERE ID = {id}')
    await conn.close()
    return delete_info