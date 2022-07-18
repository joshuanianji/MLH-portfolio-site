FROM mcr.microsoft.com/vscode/devcontainers/python:3.9

WORKDIR /myportfolio 

COPY requirements.txt .

RUN pip3 install -r requirements.txt 

COPY . .

EXPOSE 5000
