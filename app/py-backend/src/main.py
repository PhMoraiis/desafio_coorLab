from fastapi import FastAPI, HTTPException  
from models import Trip  
from services import db_dependency  
from typing import List 

app = FastAPI()  

@app.get("/")  
async def root():
    return {"message": "Hello World"} 

@app.get("/trips/")
# Definindo os parâmetros para a rota
async def find_trip(city: str, db: db_dependency):  
    # Consultando viagens para a cidade especificada no banco de dados
    city_trips = db.query(Trip).filter(Trip.city == city).all()  

    # Se não houver viagens encontradas para a cidade especificada
    if not city_trips:  
        raise HTTPException(status_code=404, detail="Nenhuma viagem encontrada para a cidade especificada") 

    # Inicializando variáveis para a duração mais curta e o preço mais barato
    shortest_duration = None  
    cheapest_price = None
    shortest_duration_trip = None
    cheapest_price_trip = None

    # Iterando sobre cada viagem para a cidade especificada
    for trip in city_trips:  
        # Extraindo informações de duração e preço da viagem
        duration_str = trip.duration  
        price_str = trip.price_economy

        # Extraindo o valor numérico da string de duração
        duration_value = int(duration_str[:-1])  
        # Extraindo o valor numérico da string de preço
        price_value = float(price_str[3:])  

        # Atualizando a viagem com a duração mais curta
        if shortest_duration is None or duration_value < shortest_duration: 
            shortest_duration = duration_value
            shortest_duration_trip = trip

        # Atualizando a viagem com o preço mais barato
        if cheapest_price is None or price_value < cheapest_price:  
            cheapest_price = price_value
            cheapest_price_trip = trip

    # Lidando com o caso em que a viagem com a duração mais curta tem a mesma duração que a viagem mais barata
    if shortest_duration_trip.duration == cheapest_price_trip.duration: 
        # Atualizando a viagem com a duração mais curta com base no preço do conforto
        shortest_duration_trip = min(city_trips, key=lambda x: float(x.price_confort[3:]))  

    return {
        "trip_shortest_duration": { 
            "name": shortest_duration_trip.name,
            "city": shortest_duration_trip.city,
            "duration": shortest_duration_trip.duration,
            "price_confort": shortest_duration_trip.price_confort,
            "price_economy": shortest_duration_trip.price_economy,
            "seat": shortest_duration_trip.seat,
            "bed": shortest_duration_trip.bed
        },
        "trip_cheapest": {  
            "name": cheapest_price_trip.name,
            "city": cheapest_price_trip.city,
            "duration": cheapest_price_trip.duration,
            "price_economy": cheapest_price_trip.price_economy,
            "seat": cheapest_price_trip.seat
        }
    }

@app.get("/cities/", response_model=List[str])  
async def get_available_cities(db: db_dependency):
    # Consultando cidades distintas no banco de dados
    cities = db.query(Trip.city).distinct().all()  
    return [city[0] for city in cities]  

@app.post("/adddatajson")  
async def add_data_from_json(data: dict, db: db_dependency): 
    try:
        # Iterando sobre os dados das viagens fornecidas em JSON
        for trip in data.get('transport', []):  
            # Criando um objeto Trip a partir dos dados
            db_trip = Trip(**trip)  
            db.add(db_trip)
        
        db.commit() 
        
        return {"message": "Dados adicionados com sucesso!"}  
    except Exception as e:
        # Desfazendo as alterações em caso de exceção
        db.rollback() 
        raise HTTPException(status_code=500, detail=str(e)) 
