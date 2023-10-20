from fastapi import APIRouter, Request

def setup_router() -> APIRouter:
    router = APIRouter(tags=["bot"])
    @router.get("/health")
    async def health():
        return {"status": "ok"}

    @router.post("/")
    async def bot(request: Request):
        return {"status": "ok"}

    return router
