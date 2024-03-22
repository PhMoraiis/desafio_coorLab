# Usa a imagem oficial do Python 3.8 como base
FROM python:3.8

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia todos os arquivos do diretório atual para o diretório de trabalho no container
COPY . .

# Expõe a porta 80 para acesso à API
EXPOSE 3000

# Comando para iniciar o servidor FastAPI quando o container for iniciado
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]
