# API Get Cursos - AIOHTTP
API que se conecta com uma DB de uma faculdade, com informações sobre cursos disponíveis.
DB feito com Postgresql, API feita com Python utilizando as bibliotecas AIOHTTP e ASYNCPG.
A escola em questão é totalmente fictícia, e a elaboração desse projeto vem apenas com o intuito de estudar sobre concorrência com Python.

## Requisitos
- Python 3

- aiohttp
> pip install aiohttp

- asyncpg
> pip install asyncpg

## Como Usar

- Inserir novo Curso:
>POST
>Aceita JSON (Exemplo abaixo)
>http://localhost:8080/insere/curso

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


- Para pegar todos os cursos:
>GET
>http://localhost:8080/cursos




