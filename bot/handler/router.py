from fastapi import APIRouter, Request, Response
from .cmd import verification_handler, event_handler

def setup_router() -> APIRouter:
    router = APIRouter(tags=["bot"])
    @router.get("/health")
    async def health():
        return {"status": "ok"}

    @router.post("/")
    async def bot(request: Request) -> Response:
        headers = request.headers
        event = verification_handler(headers)
        return event_handler(event, await request.json())

    return router
