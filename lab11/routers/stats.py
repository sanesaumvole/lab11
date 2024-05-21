from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_stats():
    return {"message": "Use /stats endpoint in main app to get the stats"}
