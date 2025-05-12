# from fastapi import APIRouter

# router = APIRouter()

# @router.get("/test")
# async def test_endpoint():
#     return {"message": "Endpoint funcionando!"}

from fastapi import APIRouter

router = APIRouter()

@router.post("/analyze")
async def analyze_data(data: dict):
    return {"result": f"Processed: {data}"}  