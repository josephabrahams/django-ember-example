# django-ember-example

## Requirements
- Python 3.7
- Node 10.15.1
- Pipenv
- nvm
- foreman, honcho, node-foreman...

## Installation
```bash
$ cp .env.example .env
$ pipenv install
$ pipenv run python manage.py migrate
$ nvm use
$ cd /client
$ npm install
```

## Local development

_Again, you can use whichever port of foreman you prefer to start the Procfile_

```bash
$ pipenv shell
$ foreman start -f Procfile.dev
```
