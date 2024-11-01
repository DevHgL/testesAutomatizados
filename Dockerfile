# Usando uma imagem base do Python
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar os arquivos de requirements (dependências) e código para o container
COPY requirements.txt requirements.txt
COPY . .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Comando para rodar os testes com pytest
CMD ["pytest"]
