from datetime import datetime

USUARIO = "gabytest"

print("--------------------------------")
print("RESPUESTA AL INCIDENTE")
print("--------------------------------")

# Momento en que el incidente fue detectado
momento_deteccion = datetime.strptime(
    "2026-11-08 08:16:09",
    "%Y-%m-%d %H:%M:%S"
)

print(f"Usuario afectado: {USUARIO}")
print(f"Momento de detección: {momento_deteccion}")

# Simulación de respuesta: bloqueo del usuario
print("Acción ejecutada: BLOQUEO DE USUARIO")

estado = "BLOQUEADO"

momento_respuesta = datetime.now()

mttr = (
    momento_respuesta - momento_deteccion
).total_seconds()

with open("respuesta.log", "a", encoding="utf-8") as archivo:
    archivo.write(
        f"{momento_respuesta.strftime('%Y-%m-%d %H:%M:%S')} | "
        f"USUARIO_BLOQUEADO | {USUARIO} | "
        f"MTTR={mttr:.2f} segundos\n"
    )

print(f"Estado final: {estado}")
print(f"Momento de respuesta: {momento_respuesta}")
print(f"MTTR: {mttr:.2f} segundos")
print("Respuesta registrada en respuesta.log")