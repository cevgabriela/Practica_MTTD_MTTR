from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import re
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)


def conectar_db():
    return sqlite3.connect("usuarios.db")


def registrar_evento(tipo, usuario):
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("eventos.log", "a", encoding="utf-8") as archivo:
        archivo.write(f"{fecha_hora} | {tipo} | {usuario}\n")


@app.route("/")
def inicio():
    return redirect(url_for("login"))


@app.route("/registro", methods=["GET", "POST"])
def registro():

    if request.method == "POST":
        usuario = request.form["usuario"].strip()
        correo = request.form["correo"].strip().lower()
        contrasena = request.form["contrasena"]

        # Validacion del usuario:
        # Entre 4 y 20 caracteres.
        # Solo letras, numeros y guion bajo.
        if not re.match(r"^[A-Za-z0-9_]{4,20}$", usuario):
            return (
                "El usuario debe tener entre 4 y 20 caracteres "
                "y contener unicamente letras, numeros y guion bajo."
            )

        # Validacion del correo electronico
        patron_correo = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        if not re.match(patron_correo, correo):
            return "El correo electronico no es valido."

        # Validacion de la contrasena
        if len(contrasena) < 8:
            return "La contrasena debe tener al menos 8 caracteres."

        # La contrasena se almacena mediante hash
        contrasena_hash = generate_password_hash(contrasena)

        conexion = conectar_db()
        cursor = conexion.cursor()

        try:
            # Consulta parametrizada para evitar inyeccion SQL
            cursor.execute(
                """
                INSERT INTO usuarios (usuario, correo, contrasena)
                VALUES (?, ?, ?)
                """,
                (usuario, correo, contrasena_hash)
            )

            conexion.commit()

        except sqlite3.IntegrityError:
            return "El usuario o correo ya se encuentra registrado."

        finally:
            conexion.close()

        return redirect(url_for("login"))

    return render_template("registro.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        usuario = request.form["usuario"].strip()
        contrasena = request.form["contrasena"]

        conexion = conectar_db()
        cursor = conexion.cursor()

        # Consulta parametrizada
        cursor.execute(
            "SELECT contrasena FROM usuarios WHERE usuario = ?",
            (usuario,)
        )

        resultado = cursor.fetchone()

        conexion.close()

        if resultado and check_password_hash(
            resultado[0],
            contrasena
        ):
            registrar_evento("LOGIN_CORRECTO", usuario)
            return "Inicio de sesion correcto."

        registrar_evento("LOGIN_FALLIDO", usuario)
        return "Usuario o contrasena incorrectos."

    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)