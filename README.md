# Sistema de Controle de Cadastro de Empersas, Departamentos e Funcionários
Este projeto foi desenvolvido como parte de um teste de vaga, com o objetivo de criar uma plataforma de controle de cadastro de funcionários, departametnos e empresas. O sistema é construído usando Python com o framework Django e utiliza o Django Rest Framework para criar uma API RESTful.

## Requisitos
- Python 3.x
- Django
- Django Rest Framework
- PostgreSQL

## Guia de Instalação

certifique-se que tenha um ambiente com Python e PostgreSQL instalado

### Banco de Dados

O banco de dados utilizado foi PostgreSQL. Instale o Postgres na sua máquina e crie um usuário e um banco para a aplicação

criação de usuário
``` sql
CREATE ROLE backendapi SUPERUSER LOGIN PASSWORD 'backendapi';
```

Criação do banco de dados
``` sql
CREATE DATABASE backendapi OWNER backendapi;
```

### Aplicação

Acessse o projeto que está versionado no GitHub https://github.com/marcoshiroshi/backend_api

faça download do projeto na sua máquina
```
git clone https://github.com/marcoshiroshi/backend_api.git
```

instale as dependências do projeto que estão no arquivo requirements.txt
```
pip install -r 'requirements.txt'
```

com as dependências instaladas, acesse a raiz do projeto e execute o comando de criação das tabelas do banco de dados
```
python manage.py migrate
```

Crie um usuário usando o comando abaixo, você deverá criar e confimar uma senha após esse passo
```
python manage.py createsuperuser --username=exemplo --email=exemplo@example.com
```

Após o sistema ser instalado e configurado, ele já pode ser acessado. Utilize o comando para iniciar o servidor localmente
```
python manage.py runserver
```



## End Points e Saídas 

### Raiz da Aplicação

- **Método:** GET
- **Endpoint:** `/`
- **Saída:** 
```json
{
    "empresas": "http://127.0.0.1:8000/empresas/",
    "departamentos": "http://127.0.0.1:8000/departamentos/",
    "pessoas": "http://127.0.0.1:8000/pessoas/"
}
```

### Login

- **Método:** POST
- **Endpoint:** `/api-auth/login/?next=/`

### Logout

- **Método:** POST
- **Endpoint:** `/api-auth/logout/?next=/`

### Listar Todas as Empresas, Departamentos ou Pessoas

- **Método:** GET
- **Endpoint:** `/empresas/`
- **Saída:** 
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "url": "http://127.0.0.1:8000/empresas/1/",
            "id": 1,
            "cnpj": "26637479000165",
            "logradouro": "Paranoá, Quadra 8 Conjunto Q",
            "cidade": "Lagos",
            "pais": "Brasil",
            "ativo": true
        }
    ]
}
```
- **Endpoint:** `/departamentos/`
- **Saída:** 
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "url": "http://127.0.0.1:8000/departamentos/1/",
            "id": 1,
            "centro_custo": "123456789",
            "nome": "financeiro",
            "codigo_integracao": "123456789",
            "ativo": true,
            "empresa": "http://127.0.0.1:8000/empresas/1/"
        }
    ]
}
```

- **Endpoint:** `/pessoas/`
- **Saída:** 
```json
{
    "count": 1,
    "next": "http://127.0.0.1:8000/pessoas/",
    "previous": null,
    "results": [
        {
            "url": "http://127.0.0.1:8000/pessoas/2/",
            "nome_completo": "marcos hiroshi souza mori 22",
            "email_contato": "abc@123.com",
            "telefone": "(11) 23132-1123",
            "data_nascimento": "2023-11-25",
            "data_ingresso": "2023-11-14",
            "data_desligamento": null,
            "ativo": false,
            "cidade": "São Paulo",
            "departamento": "http://127.0.0.1:8000/departamentos/1/",
            "empresa": "http://127.0.0.1:8000/empresas/1/"
        }
    ]
}
```

### Criar um Nova Empresas, Departamentos ou Pessoas

- **Método:** POST
- **Endpoint:** `/empresas/`
- **Saída:** 
```json
{
    "url": "http://127.0.0.1:8000/empresas/2/",
    "id": 2,
    "cnpj": "50552538000187",
    "logradouro": "Conquista, Rua Botafogo",
    "cidade": "Toronto",
    "pais": "Austrália",
    "ativo": true
}
```

- **Endpoint:** `/departamentos/`
- **Saída:** 
```json
{
    "url": "http://127.0.0.1:8000/departamentos/3/",
    "id": 3,
    "centro_custo": "centro 3",
    "nome": "recepção",
    "codigo_integracao": "112345689",
    "ativo": true,
    "empresa": "http://127.0.0.1:8000/empresas/2/"
}
```

- **Endpoint:** `/pessoas/`
- **Saída:** 
```json
{
    "url": "http://127.0.0.1:8000/pessoas/16/",
    "nome_completo": "joão júniior januário",
    "email_contato": "teste@gmail.com",
    "telefone": "(11) 23132-1123",
    "data_nascimento": "2023-10-30",
    "data_ingresso": "2023-11-27",
    "data_desligamento": null,
    "ativo": true,
    "cidade": "Guadalajara",
    "departamento": "http://127.0.0.1:8000/departamentos/3/",
    "empresa": "http://127.0.0.1:8000/empresas/1/"
}
```

### Recuperar Detalhes de uma Empresas, Departamentos ou Pessoas Específica

- **Método:** GET
- **Endpoint:** `/empresas/{id}/`
- **Saída:** 
```json
{
    "url": "http://127.0.0.1:8000/empresas/1/",
    "id": 1,
    "cnpj": "26637479000165",
    "logradouro": "Paranoá, Quadra 8 Conjunto Q",
    "cidade": "Lagos",
    "pais": "Brasil",
    "ativo": true
}
```

- **Endpoint:** `/departamentos/{id}/`
- **Saída:** 
```json
{
    "url": "http://127.0.0.1:8000/departamentos/1/",
    "id": 1,
    "centro_custo": "123456789",
    "nome": "financeiro",
    "codigo_integracao": "123456789",
    "ativo": true,
    "empresa": "http://127.0.0.1:8000/empresas/1/"
}
```

- **Endpoint:** `/pessoas/{id}/`
- **Saída:** 
```json
{
    "url": "http://127.0.0.1:8000/pessoas/2/",
    "nome_completo": "marcos hiroshi souza mori 22",
    "email_contato": "abc@123.com",
    "telefone": "(11) 23132-1123",
    "data_nascimento": "2023-11-25",
    "data_ingresso": "2023-11-14",
    "data_desligamento": null,
    "ativo": false,
    "cidade": "São Paulo",
    "departamento": "http://127.0.0.1:8000/departamentos/1/",
    "empresa": "http://127.0.0.1:8000/empresas/1/"
}
```

### Atualizar Detalhes de uma Empresa, Departamento ou Pessoa Específica

- **Método:** PUT ou PATCH
- **Endpoint:** `/empresas/{id}/`
- **Saída:** 
```json
{
    "url": "http://127.0.0.1:8000/empresas/1/",
    "id": 1,
    "cnpj": "26637479000165",
    "logradouro": "Paranoá, Quadra 8 Conjunto Q",
    "cidade": "Lagos",
    "pais": "Brasil",
    "ativo": true
}
```

- **Endpoint:** `/departamentos/{id}/`
- **Saída:** 
```json
{
    "url": "http://127.0.0.1:8000/departamentos/1/",
    "id": 1,
    "centro_custo": "123456789",
    "nome": "financeiro",
    "codigo_integracao": "123456789",
    "ativo": true,
    "empresa": "http://127.0.0.1:8000/empresas/1/"
}
```

- **Endpoint:** `/pessoas/{id}/`
- **Saída:** 
```json
{
    "url": "http://127.0.0.1:8000/pessoas/2/",
    "nome_completo": "marcos hiroshi souza mori 22",
    "email_contato": "abc@123.com",
    "telefone": "(11) 23132-1123",
    "data_nascimento": "2023-11-25",
    "data_ingresso": "2023-11-14",
    "data_desligamento": null,
    "ativo": false,
    "cidade": "São Paulo",
    "departamento": "http://127.0.0.1:8000/departamentos/1/",
    "empresa": "http://127.0.0.1:8000/empresas/1/"
}
```

### Excluir uma Empresa, Departamento ou Pessoa Específica

- **Método:** DELETE
- **Endpoint:** `/empresas/{id}/`
- **Endpoint:** `/departamentos/{id}/`
- **Endpoint:** `/pessoas/{id}/`

### Filtrar Pessoas por Parâmetros (por exemplo, empresa, departamento ou cidade)

- **Método:** GET
- **Endpoint:** `/pessoas/?empresa={cnpj}&departamento={centro de custo}&cidade={nome da cidade}`
- - **Saída:** 
```json
{
    "count": 13,
    "next": "http://127.0.0.1:8000/pessoas/?cidade=s%C3%A3o&departamento=1&empresa=26637479000165&page=2",
    "previous": null,
    "results": [
        {
            "url": "http://127.0.0.1:8000/pessoas/1/",
            "nome_completo": "marcos hiroshi souza mori",
            "email_contato": "abc@123.com",
            "telefone": "(11) 23132-1123",
            "data_nascimento": "2023-11-25",
            "data_ingresso": "2023-11-14",
            "data_desligamento": null,
            "ativo": false,
            "cidade": "São Paulo",
            "departamento": "http://127.0.0.1:8000/departamentos/1/",
            "empresa": "http://127.0.0.1:8000/empresas/1/"
        },
        {
            "url": "http://127.0.0.1:8000/pessoas/2/",
            "nome_completo": "marcos hiroshi souza mori 22",
            "email_contato": "abc@123.com",
            "telefone": "(11) 23132-1123",
            "data_nascimento": "2023-11-25",
            "data_ingresso": "2023-11-14",
            "data_desligamento": null,
            "ativo": false,
            "cidade": "São Paulo",
            "departamento": "http://127.0.0.1:8000/departamentos/1/",
            "empresa": "http://127.0.0.1:8000/empresas/1/"
        },
        {
            "url": "http://127.0.0.1:8000/pessoas/4/",
            "nome_completo": "marcos hiroshi souza mori 2233",
            "email_contato": "teste@teste.com",
            "telefone": "(11) 23132-1123",
            "data_nascimento": "2023-11-13",
            "data_ingresso": "2023-11-28",
            "data_desligamento": null,
            "ativo": true,
            "cidade": "São Paulo",
            "departamento": "http://127.0.0.1:8000/departamentos/1/",
            "empresa": "http://127.0.0.1:8000/empresas/1/"
        },
        {
            "url": "http://127.0.0.1:8000/pessoas/5/",
            "nome_completo": "marcos hiroshi souza mori 2233",
            "email_contato": "teste@teste.com",
            "telefone": "(11) 23132-1123",
            "data_nascimento": "2023-11-13",
            "data_ingresso": "2023-11-28",
            "data_desligamento": null,
            "ativo": true,
            "cidade": "São Paulo",
            "departamento": "http://127.0.0.1:8000/departamentos/1/",
            "empresa": "http://127.0.0.1:8000/empresas/1/"
        },
        {
            "url": "http://127.0.0.1:8000/pessoas/6/",
            "nome_completo": "marcos hiroshi souza mori 2233",
            "email_contato": "teste@teste.com",
            "telefone": "(11) 23132-1123",
            "data_nascimento": "2023-11-13",
            "data_ingresso": "2023-11-28",
            "data_desligamento": null,
            "ativo": true,
            "cidade": "São Paulo",
            "departamento": "http://127.0.0.1:8000/departamentos/1/",
            "empresa": "http://127.0.0.1:8000/empresas/1/"
        },
        {
            "url": "http://127.0.0.1:8000/pessoas/7/",
            "nome_completo": "marcos hiroshi souza mori 2233",
            "email_contato": "teste@teste.com",
            "telefone": "(11) 23132-1123",
            "data_nascimento": "2023-11-13",
            "data_ingresso": "2023-11-28",
            "data_desligamento": null,
            "ativo": true,
            "cidade": "São Paulo",
            "departamento": "http://127.0.0.1:8000/departamentos/1/",
            "empresa": "http://127.0.0.1:8000/empresas/1/"
        },
        {
            "url": "http://127.0.0.1:8000/pessoas/8/",
            "nome_completo": "marcos hiroshi souza mori 2233",
            "email_contato": "teste@teste.com",
            "telefone": "(11) 23132-1123",
            "data_nascimento": "2023-11-13",
            "data_ingresso": "2023-11-28",
            "data_desligamento": null,
            "ativo": true,
            "cidade": "São Paulo",
            "departamento": "http://127.0.0.1:8000/departamentos/1/",
            "empresa": "http://127.0.0.1:8000/empresas/1/"
        },
        {
            "url": "http://127.0.0.1:8000/pessoas/9/",
            "nome_completo": "marcos hiroshi souza mori 2233",
            "email_contato": "teste@teste.com",
            "telefone": "(11) 23132-1123",
            "data_nascimento": "2023-11-13",
            "data_ingresso": "2023-11-28",
            "data_desligamento": null,
            "ativo": true,
            "cidade": "São Paulo",
            "departamento": "http://127.0.0.1:8000/departamentos/1/",
            "empresa": "http://127.0.0.1:8000/empresas/1/"
        },
        {
            "url": "http://127.0.0.1:8000/pessoas/10/",
            "nome_completo": "marcos hiroshi souza mori 2233",
            "email_contato": "teste@teste.com",
            "telefone": "(11) 23132-1123",
            "data_nascimento": "2023-11-13",
            "data_ingresso": "2023-11-28",
            "data_desligamento": null,
            "ativo": true,
            "cidade": "São Paulo",
            "departamento": "http://127.0.0.1:8000/departamentos/1/",
            "empresa": "http://127.0.0.1:8000/empresas/1/"
        },
        {
            "url": "http://127.0.0.1:8000/pessoas/11/",
            "nome_completo": "marcos hiroshi souza mori",
            "email_contato": "teste@teste.com",
            "telefone": "(11) 23132-1123",
            "data_nascimento": "2023-12-08",
            "data_ingresso": "2023-11-11",
            "data_desligamento": "2023-11-02",
            "ativo": false,
            "cidade": "São Paulo",
            "departamento": "http://127.0.0.1:8000/departamentos/1/",
            "empresa": "http://127.0.0.1:8000/empresas/1/"
        }
    ]
}
```