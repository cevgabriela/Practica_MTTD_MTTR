## Laboratorio: Código Seguro y Modelo OWASP

### 1. Datos generales

- **Nombre completo:** Verónica Gabriela Cevallos Delgado
- **Carné:** No asignado
- **Correo institucional:** cevgabriela@gmail.com
- **Asignatura:** Lenguajes de Programación con Aspectos de Seguridad 03-2026
- **Fecha:** 08/11/2026

### 2. Descripción

Este laboratorio consiste en desarrollar una aplicación web utilizando Python y Flask, implementando controles básicos de seguridad basados en buenas prácticas y el modelo OWASP.

Se aplican mecanismos de validación de entradas, consultas parametrizadas, protección de contraseñas mediante hash, prevención de usuarios duplicados, registro de eventos de autenticación y detección de incidentes.

Adicionalmente, se implementa la detección de tres intentos fallidos de inicio de sesión, una respuesta simulada mediante el bloqueo del usuario y el cálculo de las métricas MTTD (Mean Time To Detect) y MTTR (Mean Time To Respond).

### 3. Estructura del proyecto

Practica_MTTD_MTTR/
├── templates/
│   ├── login.html
│   └── registro.html
├── .gitignore
├── app.py
├── crearDB.py
├── detector.py
├── eventos.log
├── requirements.txt
├── respuesta.log
├── respuesta.py
├── usuarios.db
└── README.md

La carpeta `venv/` corresponde al entorno virtual local y está excluida del repositorio mediante `.gitignore`.

### 4. Ejecución del proyecto

**Paso 1. Clonar el repositorio**

git clone URL_DEL_REPOSITORIO

**Paso 2. Ingresar al proyecto**

cd Practica_MTTD_MTTR

**Paso 3. Crear un entorno virtual**

python -m venv venv

**Paso 4. Activar el entorno virtual**

En Windows:

venv\Scripts\activate

**Paso 5. Instalar las dependencias**

pip install -r requirements.txt

**Paso 6. Crear la base de datos**

python crearDB.py

**Paso 7. Ejecutar la aplicación**

python app.py

La aplicación estará disponible en:

http://127.0.0.1:5000

**Paso 8. Ejecutar el detector de incidentes**

Después de generar al menos tres intentos fallidos de inicio de sesión:

python detector.py

El detector identifica el incidente, calcula el MTTD, simula el bloqueo del usuario, calcula el MTTR y registra la respuesta en `respuesta.log`.

### 5. Resultados de las pruebas

Se realizaron tres escenarios controlados de intentos fallidos de autenticación.

| Escenario | MTTD | MTTR |
|---|---:|---:|
| 1 | 206.08 segundos | 305.60 segundos |
| 2 | 231.02 segundos | 168.47 segundos |
| 3 | 47.68 segundos | 69.91 segundos |
| **Promedio** | **161.59 segundos** | **181.33 segundos** |

El MTTD promedio obtenido fue de aproximadamente 2 minutos y 42 segundos.

El MTTR promedio obtenido fue de aproximadamente 3 minutos y 1 segundo