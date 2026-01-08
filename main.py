from fastapi import FastAPI
from faststream.rabbit.fastapi import RabbitRouter

app = FastAPI()
router = RabbitRouter("amqp://guest:guest@localhost:5674")

@router.post("/notific")
async def make_order(name: str):
    await router.broker.publish(
            f"Новое уведомление: {name}",
            queue="notific",
        )
    return {"data" : "OK"}

app.include_router(router)