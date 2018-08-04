# Sorting Service

## Para rodar o projeto em um docker:

__Em linux__: com o terminal aberto no diretório da aplicação digite:
```
sudo docker build -t test-stormtech .
```

Com o término do build digite:
```
sudo docker run -p 8000:8000 test-stormtech
```

Após isso é só acessar a porta 8000 de seu localhost.

## Para rodar o projeto usando uma env em python:
__pré-requisitos:__
* Ter o Python3 instalado;
* Ter o pip do python3 instalado;

Caso você não tenha a virtualenv instalada, basta inserir no terminal:

```
pip3 install virtualenv
```

Abra o terminal na raiz do diretório e crie uma env:

```
virtualenv -p python3 env
```

Ative sua env:

__linux:__
```
source env/bin/activate
```

__windows:__
```
env\Scripts\activate
```

Com sua env ativa, você deve instalar as dependências:
```
pip install -r requirements.txt
```

Agora o sistema está configurado para executar. Para executar no terminal:
```
python manage.py runserver
```

Neste caso você precisará sempre ativar a sua env para rodar a aplicação, pois nela conterá todas as dependências necessárias para sua execução. Com uma env você terá um ambiente para rodar sua aplicação sem instalar as bibliotecas de maneira solta em sua máquina. Obs: Dentro de uma env não é necessário dizer a versão do python que está sendo usada já que ela foi inicializada com uma versão base.

## Endpoints da aplicação

__Cadastrar um livro__
```
POST http://localhost:8000/book
```
*Para visualizar o payload acesse: http://localhost:8000/docs*

__Selecionar todos os livros__
```
GET http://localhost:8000/book
```

__Selecionar um livro__
```
GET http://localhost:8000/book/{id}
```

__Ordenar por propriedade do livro__
```
GET http://localhost:8000/book?filter=title
```
*Filtro pode ser: title, author ou edition_year*

## Executar testes

Dentro da env:
```
python manage.py test
```
