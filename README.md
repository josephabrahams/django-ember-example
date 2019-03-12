# dj-super-rentals
A simple app to demonstrate how to integrate Django & Ember.

Based on: <https://guides.emberjs.com/release/tutorial/ember-cli/>.

## Requirements
- Python 3.7
- Node 10.15.1
- PostgreSQL
- [Pipenv](https://pipenv.readthedocs.io/en/latest/)
- [nvm](https://github.com/creationix/nvm)
- [foreman](https://github.com/ddollar/foreman) or similar (e.g. forego, node-foreman, honcho)

## Installation
```bash
$ cp .env.example .env
$ createdb superrentals
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
