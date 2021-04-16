from .connection import get_conn
import datetime

async def put_curso_db(data):
    conn = await get_conn()

    data = verif_boolean(data)

    atualizacoes = await conn.execute(f"""
        UPDATE cursos SET 
            CURSO = $1,
            NOME = $2,
            MENSALIDADE = $3, 
            DURACAO = $4,
            DESCRICAO = $5,
            DATA_INICIO = $6,
            HABILITADO = $7 WHERE ID = $8
            
        
    """, data['curso'], data['nome'],
    data['mensalidade'], data['duracao'],
    data['descricao'], get_data(data['data_inicio']),
    data['habilitado'], data['id'])

    await conn.close()

    return atualizacoes
    

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