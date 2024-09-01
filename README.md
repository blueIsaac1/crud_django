# Projeto Django com SQLite3

Bem-vindo ao projeto Django com SQLite3! Este é um projeto de exemplo que utiliza o Django, um framework web de alto nível para Python, e o SQLite3, um banco de dados leve e integrado.

## Sumário

- [Descrição](#descrição)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Uso](#uso)

## Descrição

Este projeto é uma aplicação web simples desenvolvida com o framework Django e utiliza o banco de dados SQLite3 para armazenar dados. O objetivo é demonstrar a configuração básica de um projeto Django com uma configuração padrão do SQLite com ferramentar CRUD (Create, Read Update e Delete).

## Pré-requisitos

Antes de começar, certifique-se de ter o Python e o pip instalados em sua máquina. Recomenda-se também criar um ambiente virtual para gerenciar as dependências do projeto.

## Instalação

Siga os passos abaixo para configurar o projeto em seu ambiente local:

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/blueIsaac1/crud_django.git
    cd seu-repositorio
    ```

2. **Crie e ative um ambiente virtual:**

    ```bash
    python -m venv venv
    source venv/bin/activate   # Para Linux/MacOS
    venv\Scripts\activate      # Para Windows
    ```

3. **Instale as dependências:**

    ```bash
    pip install -r req.txt
    ```

4. **Aplique as migrações do banco de dados:**

    ```bash
    python manage.py migrate
    ```

5. **Crie um superusuário para acessar o painel administrativo (opcional):**

    ```bash
    python manage.py createsuperuser
    ```

6. **Inicie o servidor de desenvolvimento:**

    ```bash
    python manage.py runserver
    ```

7. **Acesse a aplicação:**

    Abra seu navegador e vá para `http://127.0.0.1:8000/`. Para acessar o painel administrativo, vá para `http://127.0.0.1:8000/admin/` e faça login com as credenciais do superusuário que você criou.
## Uso
8. **Imagens:**
# 1:
![crud1](https://github.com/blueIsaac1/crud_django/assets/144810253/65cfde00-72c2-4223-8cee-26acbb98ed3a)
# 2:
![crud2](https://github.com/blueIsaac1/crud_django/assets/144810253/41769341-2c54-4b43-bfe3-5eaeedef838b)
# 3:
![crud3](https://github.com/blueIsaac1/crud_django/assets/144810253/0338b2ce-fc52-4a72-9033-50aaf89b6389)
# 4:
![crud4-update](https://github.com/blueIsaac1/crud_django/assets/144810253/5492defa-9501-4d5c-b794-abf1322086a0)
