from connection import get_conn
import asyncio

async def create_table(data):
    conn = await get_conn()

    info = await conn.execute(data)
    print(info)
    
    await conn.close()
    


commands_table_cursos = (
        """
        CREATE TABLE cursos (
            id SERIAL PRIMARY KEY,
            curso VARCHAR(25),
            nome VARCHAR(150),
            mensalidade DECIMAL(6,2),
            duracao VARCHAR(50),
            descricao VARCHAR(500),
            data_inicio DATE,
            habilitado BOOLEAN
        )
        """)

def main(commands):
    loop = asyncio.get_event_loop()
    asyncio.run(create_table(commands))


main(commands_table_cursos)