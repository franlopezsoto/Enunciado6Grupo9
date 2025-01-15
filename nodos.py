import requests
import time
import random

base_url = "http://127.0.0.1:8000"

def increment_node(node_id):
    """
    Nodo que incrementa el contador.
    """
    try:
        response = requests.post(f"{base_url}/increment", json={"increment_by": 1, "node_id": node_id})
        print(f"Nodo {node_id}: Respuesta al incrementar:", response.json())
    except Exception as e:
        print(f"Nodo {node_id}: Error al incrementar:", e)

if __name__ == "__main__":
    print("Nodos 1, 2 y 3: Incrementando el contador.")
    while True:
        node_id = random.choice([1, 2, 3])
        increment_node(node_id)
        time.sleep(random.uniform(0.5, 2))  # Simulación de tiempo entre solicitudes
