# API Get Cursos - AIOHTTP
API que se conecta com uma DB de uma faculdade, com informações sobre cursos disponíveis.
DB feito com Postgresql, API feita com Python utilizando as bibliotecas AIOHTTP e ASYNCPG.
A escola em questão é totalmente fictícia, e a elaboração desse projeto vem apenas com o intuito de estudar sobre concorrência com Python.

## Status do Projeto
Em andamento

## Requisitos
- Python 3

- aiohttp
> pip install aiohttp

- asyncpg
> pip install asyncpg

## Como Usar

- Inserir novo Curso:
>POST: Aceita JSON - 
>http://localhost:8080/insere/curso

>{
        "curso": "CPB2",
        "nome": "Curso de Python Básico 2",
        "mensalidade": "120.00",
        "duracao": "6 meses",
        "descricao": "Lorem Ipsum, dolor ao simet, me forteri no dolor del le ipsum met",
        "data_inicio": "2021-07-01",
        "habilitado": null
    }


- Para pegar todos os cursos:
>GET
>http://localhost:8080/cursos

- Para pegar apenas 1 curso específico pela ID:
>GET
>http://localhost:8080/curso/{id}

- Para atualizar um curso específico:
>PUT: Aceita JSON - Enviar id do curso -
http://localhost:8080/atualiza/curso

>{
        "id": 2,
        "curso": "CPB2",
        "nome": "Curso de Python Básico 2",
        "mensalidade": "120.00",
        "duracao": "6 meses",
        "descricao": "Lorem Ipsum, dolor ao simet, me forteri no dolor del le ipsum met",
        "data_inicio": "2021-07-01",
        "habilitado": null
    }

- Para deletar curso específico pelo ID:
>DELETE
>http://localhost:8080/deleta/curso/{id}
