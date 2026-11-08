import sqlite3

conexion = sqlite3.connect('usuarios.db')
cursor = conexion.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT UNIQUE NOT NULL,
    correo TEXT UNIQUE NOT NULL,
    contrasena TEXT NOT NULL
)
''')

conexion.commit()
conexion.close()

print("Base de datos creada correctamente.")