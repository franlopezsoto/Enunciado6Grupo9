import requests
import time

base_url = "http://127.0.0.1:8000"

def monitor_and_reset():
    """
    Monitorea el contador y lo reinicia si alcanza el valor 9.
    """
    while True:
        response = requests.get(f"{base_url}/get_counter")
        counter_value = response.json().get("counter_value", -1)

        if counter_value == 9:
            print("Nodo 4: El contador alcanzó 9. Reiniciando...")
            reset_response = requests.post(f"{base_url}/reset")
            print("Nodo 4: Respuesta al reiniciar:", reset_response.json())

        # Esperar antes de la siguiente verificación
        time.sleep(1)

if __name__ == "__main__":
    print("Nodo 4: Monitoreando el contador...")
    monitor_and_reset()
