from fastapi import FastAPI
from threading import Lock
from pydantic import BaseModel

app = FastAPI()

# Contador compartido y su Lock
shared_counter = {"value": 0}
counter_lock = Lock()


class IncrementRequest(BaseModel):
    increment_by: int
    node_id: int


@app.post("/increment")
def increment_counter(request: IncrementRequest):
    """
    Incrementa el contador en una cantidad específica asegurando exclusión mutua.
    """
    with counter_lock:
        if shared_counter["value"] < 9:
            shared_counter["value"] += request.increment_by
            return {
                "message": f"Node {request.node_id} incremented the counter.",
                "counter_value": shared_counter["value"],
            }
        else:
            # Notificar que el contador ha alcanzado 9
            return {
                "message": "Counter reached 9. Awaiting reset.",
                "counter_value": shared_counter["value"],
            }


@app.get("/get_counter")
def get_counter():
    """
    Devuelve el valor actual del contador.
    """
    return {"counter_value": shared_counter["value"]}


@app.post("/reset")
def reset_counter():
    """
    Reinicia el contador a 0.
    """
    with counter_lock:
        shared_counter["value"] = 0
        return {"message": "Counter reset to 0.", "counter_value": shared_counter["value"]}
