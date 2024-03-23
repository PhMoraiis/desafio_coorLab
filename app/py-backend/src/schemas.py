from pydantic import BaseModel

class TripBase(BaseModel):
    name: str
    price_confort: str
    price_economy: str
    city: str
    duration: str
    seat: str
    bed: str
