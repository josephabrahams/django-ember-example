# django-ember-example

## Requirements
- Python 3.7
- Node 10.15.1
- Pipenv
- nvm
- foreman

## Installation
```bash
$ cp .env.example .env
$ pipenv install
$ pipenv run python manage.py migrate
$ nvm use
$ npm install
```

## Local development
```bash
$ pipenv shell
$ foreman start -f Procfile.dev
```
