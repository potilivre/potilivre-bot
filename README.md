# Language
- [English](https://github.com/potilivre/potilivre-bot#English-Version)
- [Português](https://github.com/potilivre/potilivre-bot#Versão-em-português)

---

# [English version](https://github.com/potilivre/potilivre-bot#English-Version)
# PotiLivre Bot
Telegram bot from the Free Software Potiguar community, PotiLivre.

## Getting Started
These instructions will get you a copy of the project up and running \
on your local machine for development and testing purposes.

### Prerequisites
The things you will need to install:
- Python 3.7
- [Pipenv](https://pipenv.readthedocs.io/en/latest/)

A step by step guide to get a development env running:

First of all, make a copy of `.env.sample` to `.env`. \
Now [generate your token](https://core.telegram.org/bots#6-botfather) and copy to `.env`

```
cp .env.sample .env
```

Install the dependencies

```
pipenv install sync
```

### Running
Enter the `pipenv` virtual environment

```
pipenv shell
```

Run bot

```
python3 bot.py
```

## Contributing
### Steps for Submitting Code
1. Fork this repository on GitHub.
2. Make your changes.
3. Send a GitHub Pull Request to the main repository’s `master` branch. GitHub \
Pull Requests are the expected method of code collaboration on this project.

---

# [Versão em português](https://github.com/potilivre/potilivre-bot#Versão-em-português)

# Bot PotiLivre
Bot de Telegram da comunidade potiguar de Software Livre, Potilivre.

## Começando
Essas instruções farão com que você tenha uma cópia do projeto e possa \
rodar localmente para fins de desenvolvimento e teste.


### Pré-requesitos
As coisas que você vai precisar instalar:

- Python 3.7
- [Pipenv](https://pipenv.readthedocs.io/en/latest/)

Guia passo à passo para rodar corretamente um "env" de desenvolvimento:

Primeiramente, faça uma cópia de `.env.sample` para `.env`. \
Agora [gere seu token](https://core.telegram.org/bots#6-botfather) e copie para `.env`.

```
cp .env.sample .env
```

Instale as dependências

```
pipenv install sync
```

### Rodando
Entre no ambiente virtual `pipenv`

```
pipenv shell
```

Rode o bot

```
python3 bot.py
```

## Contribuindo
### Passos para submeter mudanças
1. Dê um "fork" nesse repositório pelo GitHub.
2. Faça suas alterações.
3. Envie um pull request do github para o repositório principal na "branch master". \
Pull Requests são a maneira esperada de colaboração para esse projeto.
