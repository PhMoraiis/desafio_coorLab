#!/bin/bash

# Função para verificar se o Docker está instalado
check_docker_installed() {
    if ! command -v docker &> /dev/null; then
        echo "Erro: Docker não está instalado ou não é acessível."
        exit 1
    fi
}

# Função para construir e executar o frontend Vue com Docker
run_vue_frontend_with_docker() {
    echo "Construindo e iniciando o frontend Vue com Docker..."
    cd "$project_dir/app/vue-frontend" || exit
    docker build -t vue-frontend .
    docker run -d -p 8080:8080 vue-frontend
    echo "Frontend Vue está em execução na porta 8080."
}

# Função para iniciar o frontend Vue sem Docker
run_vue_frontend_without_docker() {
    echo "Iniciando o frontend Vue sem Docker..."
    cd "$project_dir/app/vue-frontend" || exit
    yarn install
    yarn dev &
    echo "Frontend Vue está em execução na porta 8080."
}

# Função para construir e executar o backend FastAPI com Docker
run_fastapi_backend_with_docker() {
    echo "Construindo e iniciando o backend FastAPI com Docker..."
    cd "$project_dir/app/py-backend/src/withDocker" || exit
    docker-compose up -d
    echo "Backend FastAPI está em execução."
}

# Função para iniciar o backend FastAPI sem Docker
run_fastapi_backend_without_docker() {
    echo "Iniciando o backend FastAPI sem Docker..."
    cd "$project_dir/app/py-backend/src/withoutDocker" || exit
    uvicorn main:app --reload --port 3000 &
    echo "Backend FastAPI está em execução na porta 3000."
}

# Verificar se o Docker está instalado
check_docker_installed

# Diretório raiz do projeto
project_dir=$(dirname "$(realpath "$0")")

# Verificar qual caso de uso está sendo utilizado
if [[ "$1" == "docker" ]]; then
    run_vue_frontend_with_docker
    run_fastapi_backend_with_docker
elif [[ "$1" == "nodocker" ]]; then
    run_vue_frontend_without_docker
    run_fastapi_backend_without_docker
else
    echo "Por favor, especifique 'docker' ou 'nodocker' como argumento para escolher o caso de uso."
    echo "Exemplo: ./run.sh docker"
    echo "ou"
    echo "Exemplo: ./run.sh nodocker"
    exit 1
fi

echo "Aplicação iniciada com sucesso!"
echo "Acesse o frontend em http://localhost:8080"
echo "Acesse a API em http://localhost:3000/docs"
