#!/bin/bash

# Verificar se o Docker está instalado
if ! command -v docker &> /dev/null; then
    echo "Erro: Docker não está instalado ou não é acessível."
    exit 1
fi

# Diretório raiz do projeto
project_dir=$(dirname "$(realpath "$0")")

# Construir e executar o frontend Vue
echo "Construindo e iniciando o frontend Vue..."
cd "$project_dir/vue-frontend/" || exit
docker build -t vue-frontend .
docker run -d -p 8080:8080 vue-frontend

# Aguardar alguns segundos para o frontend inicializar completamente
sleep 5

# Construir e executar o backend FastAPI
echo "Construindo e iniciando o backend FastAPI..."
cd "$project_dir/py-backend/" || exit
docker compose up -d

# URL do servidor FastAPI
server_url="http://localhost:3000"

# Endpoint para verificar se a API está no ar
healthcheck_endpoint="/health"

# Endpoint para adicionar dados ao banco de dados
add_data_endpoint="/adddatajson"

# Verificar se a API está no ar e totalmente funcional
echo "Verificando status da API..."
response=$(curl -sSL -w "%{http_code}" "$server_url$healthcheck_endpoint" -o /dev/null)
if [ "$response" != "200" ]; then
    echo "Erro: A API não está disponível ou funcional."
    exit 1
fi

# Aguardar um momento para os contêineres do banco de dados iniciarem completamente
echo "Aguardando inicialização dos contêineres do banco de dados..."
sleep 10

# Verificar se o contêiner do banco de dados está em execução
echo "Verificando contêiner do banco de dados..."
docker ps | grep "py-backend_db" &> /dev/null
if [ "$?" != "0" ]; then
    echo "Erro: O contêiner do banco de dados não está em execução."
    exit 1
fi

# Arquivo JSON com os dados das viagens
json_file="$project_dir/app/data.json"

# Executar a requisição POST para adicionar os dados ao banco de dados
echo "Adicionando dados ao banco de dados..."
curl -X POST -H "Content-Type: application/json" -d "@$json_file" "$server_url$add_data_endpoint"


# Exibir mensagem de conclusão
echo "Aplicação iniciada com sucesso!"
echo "Acesse o frontend em http://localhost:8080"
echo "Acesse a API em http://localhost:3000/docs"