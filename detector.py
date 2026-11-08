from datetime import datetime

ARCHIVO_EVENTOS = "eventos.log"
ARCHIVO_RESPUESTA = "respuesta.log"
UMBRAL_FALLOS = 3

intentos_fallidos = {}

# Leer los eventos registrados por la aplicacion
with open(ARCHIVO_EVENTOS, "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()

# Buscar los intentos de login fallidos
for linea in lineas:

    partes = [parte.strip() for parte in linea.split("|")]

    if len(partes) != 3:
        continue

    fecha_texto, tipo_evento, usuario = partes

    if tipo_evento == "LOGIN_FALLIDO":

        fecha_evento = datetime.strptime(
            fecha_texto,
            "%Y-%m-%d %H:%M:%S"
        )

        if usuario not in intentos_fallidos:
            intentos_fallidos[usuario] = []

        intentos_fallidos[usuario].append(fecha_evento)


# Analizar cada usuario
for usuario, intentos in intentos_fallidos.items():

    if len(intentos) >= UMBRAL_FALLOS:

        # Tomar los ultimos tres intentos para el escenario actual
        ultimos_tres = intentos[-3:]

        primer_intento = ultimos_tres[0]

        # Momento en que el incidente es detectado
        momento_deteccion = datetime.now()

        # Mean Time To Detect
        mttd = (
            momento_deteccion - primer_intento
        ).total_seconds()

        print("--------------------------------")
        print("ALERTA DE SEGURIDAD")
        print("--------------------------------")
        print(f"Usuario: {usuario}")
        print(f"Intentos fallidos: {len(ultimos_tres)}")
        print(f"Primer intento: {primer_intento}")
        print(f"Momento de deteccion: {momento_deteccion}")
        print(f"MTTD: {mttd:.2f} segundos")

        # --------------------------------
        # RESPUESTA AL INCIDENTE
        # --------------------------------

        print("--------------------------------")
        print("RESPUESTA AL INCIDENTE")
        print("--------------------------------")

        print("Accion aplicada: BLOQUEO DE USUARIO")

        # Simulacion del bloqueo
        estado = "BLOQUEADO"

        # Momento en que finaliza la respuesta
        momento_respuesta = datetime.now()

        # Mean Time To Respond
        mttr = (
            momento_respuesta - momento_deteccion
        ).total_seconds()

        print(f"Estado final: {estado}")
        print(f"Momento de respuesta: {momento_respuesta}")
        print(f"MTTR: {mttr:.2f} segundos")

        # Registrar la respuesta
        with open(
            ARCHIVO_RESPUESTA,
            "a",
            encoding="utf-8"
        ) as archivo:

            archivo.write(
                f"{momento_respuesta.strftime('%Y-%m-%d %H:%M:%S')} | "
                f"USUARIO_BLOQUEADO | {usuario} | "
                f"MTTD={mttd:.2f} segundos | "
                f"MTTR={mttr:.2f} segundos\n"
            )

        print("Respuesta registrada en respuesta.log")