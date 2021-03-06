from .connection import get_conn
import datetime

async def insert_curso(data):
    conn = await get_conn()

    data = verif_boolean(data)

    insercoes = await conn.execute("""
        INSERT INTO cursos(
            CURSO,
            NOME,
            MENSALIDADE, 
            DURACAO,
            DESCRICAO,
            DATA_INICIO,
            HABILITADO)
            VALUES ($1, $2, $3, $4, $5, $6, $7)
        
    """, data['curso'], data['nome'],
    data['mensalidade'], data['duracao'],
    data['descricao'], get_data(data['data_inicio']),
    data['habilitado'])

    await conn.close()

    return insercoes
    

def get_data(data):
    data_dia = int(data[0:4])
    data_mes = int(data[5:7])
    data_ano = int(data[8:10])
    data_formatada = datetime.date(data_dia, data_mes, data_ano)
    return data_formatada
    
def verif_boolean(data):
    habilitado = data['habilitado']
    if habilitado in ['True', 'true', 1, '1']:
        data['habilitado'] = True
    else:
        data['habilitado'] = False
    
    return data