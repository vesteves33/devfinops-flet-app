FROM python:3.12-slim

RUN apt-get update && apt-get install -y
RUN pip install --upgrade pip
RUN pip install --upgrade poetry

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && poetry install --no-root

COPY . .

#Aplicacoes Flet normalmente são expostas na porta 8080
EXPOSE 8080

#Execucao da aplicacao
CMD ["python", "app.py"]