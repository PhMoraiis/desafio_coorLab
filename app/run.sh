#!/bin/bash

# Função para verificar se o Docker está instalado
# check_docker_installed() {
#     if ! command -v docker &> /dev/null; then
#         echo "Erro: Docker não está instalado ou não é acessível."
#         exit 1
#     fi
# }

# Função para construir e executar o frontend Vue com Docker
# run_vue_frontend_with_docker() {
#     echo "Construindo e iniciando o frontend Vue com Docker..."
#     cd "vue-frontend" || exit
#     docker build -t vue-frontend .
#     docker run -d -p 8080:8080 vue-frontend
#     echo "Frontend Vue está em execução na porta 8080."
# }

# Função para construir e executar o backend FastAPI com Docker
#  run_fastapi_backend_with_docker() {
#     echo "Construindo e iniciando o backend FastAPI com Docker..."
#     cd "py-backend/src/withDocker" || exit
#     docker compose up -d
#     echo "Backend FastAPI está em execução."
# }

# Verifica qual caso de uso está sendo utilizado
# if [[ "$1" == "docker" ]]; then
#     check_docker_installed
#     run_vue_frontend_with_docker
#     run_fastapi_backend_with_docker
# elif [[ "$1" == "nodocker" ]]; then
#     run_vue_frontend_without_docker
#     run_fastapi_backend_without_docker
# else
#     echo "Por favor, especifique 'docker' ou 'nodocker' como argumento para escolher o caso de uso."
#     echo "Exemplo: ./run.sh docker"
#     echo "ou"
#     echo "Exemplo: ./run.sh nodocker"
#     exit 1
# fi

# Função para iniciar o frontend Vue sem Docker
run_vue_frontend_without_docker() {
    echo "Starting Vue frontend without Docker..."
    cd "vue-frontend" || { echo 'Erro: Diretório "vue-frontend" não encontrado.' ; exit 1; }
    yarn install || { echo 'Erro: Yarn não está instalado ou não é acessível.' ; exit 1; }
    yarn dev &
    echo "Vue frontend is running on port 8080."
}

# Função para iniciar o backend FastAPI sem Docker
run_fastapi_backend_without_docker() {
    echo "Starting FastAPI backend without Docker..."
    cd "../py-backend" || exit
    source env/bin/activate
    pip install -r requirements.txt
    cd "src/withoutDocker/" || exit
    pip install -r requirements.txt
    uvicorn main:app --reload --port 3000 &
    echo "FastAPI backend is running on port 3000."
}

# Executa o frontend Vue e o backend FastAPI sem Docker
run_vue_frontend_without_docker
run_fastapi_backend_without_docker

echo "Application started successfully!"
echo "Access the frontend at http://localhost:8080"
echo "Access the API at http://localhost:3000/docs"