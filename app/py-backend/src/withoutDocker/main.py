from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from data import transport

app = FastAPI()

# Configuração do CORS
origins = [
    "http://localhost:*",
    "http://localhost:8080",
]

# Adicionar o middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

@app.get("/")  
async def root():
    return {"message": "Hello World"} 

@app.get("/trips/")
async def find_trip(city: str):
    city_trips = [trip for trip in transport if trip["city"] == city]

    if not city_trips:
        raise HTTPException(status_code=404, detail="No trips found for the specified city")

    shortest_duration_trip = min(city_trips, key=lambda x: int(x["duration"][:-1]))
    cheapest_price_trip = min(city_trips, key=lambda x: float(x["price_economy"][3:]))

    if shortest_duration_trip["duration"] == cheapest_price_trip["duration"]:
        shortest_duration_trip = min(city_trips, key=lambda x: float(x["price_confort"][3:]))

    return {
        "trip_shortest_duration": shortest_duration_trip,
        "trip_cheapest": cheapest_price_trip
    }

@app.get("/cities/", response_model=List[str])
async def get_available_cities():
    cities = list(set(trip["city"] for trip in transport))
    return cities
