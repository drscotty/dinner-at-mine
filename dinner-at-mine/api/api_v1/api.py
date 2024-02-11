from fastapi import FastAPI, APIRouter
from models.magnet import Magnet
from data.DbContext import Session

session = Session()
api_router = APIRouter()


@api_router.post("/magnets/create")
async def create_magnet(cryostat_number: int, ):
    
    # Search for the magnet type from the database 
    magnet_type = None
    magnet = Magnet(cryostat_number=cryostat_number, magnet_type=magnet_type)
    session.add(magnet)
    

@api_router.put("/magnets/update/{id}")
async def update_magnet():
    pass


@api_router.get("/magnets/")
async def get_all_magnets() -> dict:
    magnets_query = session.query(Magnet)
    return magnets_query.all()


@api_router.get("/magnets/{magnet_id}")
async def get_magnet_by_id(magnet_id : int) -> dict:
    pass
    