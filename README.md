# dj-super-rentals
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

A simple app to demonstrate how to integrate Django & Ember.

Based on: <https://guides.emberjs.com/release/tutorial/ember-cli/>.

## Requirements
- Python 3.7
- Node 10.15
- [Pipenv](https://pipenv.readthedocs.io/en/latest/)
- [nvm](https://github.com/creationix/nvm)

## Installation
```bash
$ cp .env.example .env
$ pipenv install --dev
$ nvm install
$ pipenv run honcho run python manage.py migrate
```

## Local development
```bash
$ pipenv shell
$ nvm use
$ honcho start -f Procfile.dev
```

## Run Linters & Tests
```bash
$ honcho run npm test
```
