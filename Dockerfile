FROM python:3.7-stretch 

# I hate this but it might work
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN touch ~/.bashrc && chmod +x ~/.bashrc

# Creating app directories
RUN mkdir /app
WORKDIR /app

# Install Node
RUN mkdir -p /root/.nvm
ENV NVM_DIR /root/.nvm
RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash

# Install base Python packages we need
RUN pip install pipenv

# Add package files and install
ADD Pipfile /app
ADD Pipfile.lock /app
ADD package.json /app
ADD package-lock.json /app
ADD .nvmrc /app

# Install pip packages
RUN pipenv install

# Install specified Node version
RUN source ~/.bashrc && nvm install && nvm use

# Install npm packages
RUN mkdir -p superrentals/ember
ADD superrentals/ember/package.json superrentals/ember
ADD superrentals/ember/package-lock.json superrentals/ember
RUN source ~/.bashrc && npm run postinstall

# Add full repo
ADD . /app

# Build static assets
RUN source ~/.bashrc && npm run build

EXPOSE 8000

CMD pipenv run python manage.py runserver