# Contents
1. [English](https://github.com/potilivre/potilivre-bot#Getting Started)
2. [Portuguese](https://github.com/potilivre/potilivre-bot#Getting Started#Começando)

# PotiLivre Bot
Telegram bot from the Free Software Potiguar community, PotiLivre.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them
- Python 3.7
- [Pipenv](https://pipenv.readthedocs.io/en/latest/)

A step by step series of examples that tell you how to get a development env running

First of all, make a copy of `.env.sample` to `.env`. Now [generate your token](https://core.telegram.org/bots#6-botfather) and copy to `.env`

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

1. Fork the repository on GitHub.
2. Make your change.
3. Send a GitHub Pull Request to the main repository’s `master` branch. GitHub
Pull Requests are the expected method of code collaboration on this project.


# Começando
Essas instruções farão com que você tenha uma cópia do projeto e possa rodar
na máquina local para fins de desenvolvimento e teste.
