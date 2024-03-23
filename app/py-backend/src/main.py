from fastapi import FastAPI, HTTPException
from models import Trip
import json
from services import db_dependency

app = FastAPI()

@app.get("/searchtrip/")
async def find_trip(city: str, db: db_dependency):
   # Consultar viagens para a cidade fornecida no banco de dados
    city_trips = db.query(Trip).filter(Trip.city == city).all()

    if not city_trips:
        raise HTTPException(status_code=404, detail="Nenhuma viagem encontrada para a cidade especificada")

    shortest_duration = None
    cheapest_price = None
    shortest_duration_trip = None
    cheapest_price_trip = None

    for trip in city_trips:
        duration_str = trip.duration
        price_str = trip.price_economy

        # Extrair valores numéricos de strings de duração e preço
        duration_value = int(duration_str[:-1])  # Remove o último caractere "H" de "12H"
        price_value = float(price_str[3:])  # Remove os primeiros três caracteres "R$ " de "R$ 71.19"

        # Comparar a menor duração
        if shortest_duration is None or duration_value < shortest_duration:
            shortest_duration = duration_value
            shortest_duration_trip = trip

        # Comparar o preço mais econômico
        if cheapest_price is None or price_value < cheapest_price:
            cheapest_price = price_value
            cheapest_price_trip = trip

    # Se a duração da viagem mais barata for igual à duração da viagem mais curta,
    # atualize a viagem mais curta para a que tem o preço mais barato
    if shortest_duration_trip.duration == cheapest_price_trip.duration:
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

@app.post("/adddatajson")
async def add_data_from_json(data: dict, db: db_dependency):
    try:
        # Adiciona os dados ao banco de dados
        for trip in data.get('transport', []):
            db_trip = Trip(**trip)
            db.add(db_trip)
        
        # Realiza o commit das transações
        db.commit()
        
        return {"message": "Dados adicionados com sucesso!"}
    except Exception as e:
        # Se ocorrer algum erro, faz rollback e retorna uma mensagem de erro
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))