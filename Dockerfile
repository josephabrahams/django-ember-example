FROM python:3.7-stretch 

# Install Node
# RUN curl -sL https://deb.nodesource.com/setup_11.x | bash -
# RUN apt-get install -y nodejs
RUN mkdir -p /usr/local/nvm
ENV NVM_DIR /usr/local/nvm
RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash

# Install base Python packages we need
RUN pip install pipenv

RUN mkdir /app
WORKDIR /app

ADD Pipfile /app
ADD Pipfile.lock /app
ADD package.json /app
ADD package-lock.json /app
ADD .nvmrc /app

RUN pipenv install


RUN . $NVM_DIR/nvm.sh && nvm install 10.15
RUN npm install