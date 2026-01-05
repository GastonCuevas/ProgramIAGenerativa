# ia_generativa

Pequeño proyecto de práctica en Python y API con FastAPI.

## Contenido
- `Clase1.py`: ejemplos básicos (fechas, factorial e interés).
- `app/`: backend FastAPI (en construcción).
  - `main.py`: punto de entrada de la API.
  - `config.py`: configuración (variables de entorno, URL BD SQLite).
  - `database.py`: inicialización de base de datos (SQLModel/SQLite).

## Requisitos
- Python 3.10+

## Instalación
En PowerShell, dentro de la carpeta del proyecto:

```powershell
# (Opcional) crear y activar entorno virtual
python -m venv .venv
. .venv\Scripts\Activate.ps1

# Instalar dependencias
pip install -r requirements.txt
```

## Ejecutar la API
```powershell
uvicorn app.main:app --reload
```

Luego abre en el navegador:
- Documentación interactiva: http://127.0.0.1:8000/docs
- Root: http://127.0.0.1:8000/

## Demo Educativa: SQL Injection

Archivo: `login_demo.html` (estático) y endpoints añadidos en `app/main.py`.

Endpoints:
- `POST /insecure_login`  -> Concatena directamente la entrada en la query: vulnerable.
- `POST /secure_login`    -> Usa filtrado ORM/parametrizado (SQLModel), evita inyección.

Modelo de usuario inicial (`app/database.py`): se crea usuario `gaston` / `1234` al iniciar si la tabla está vacía.

Ejemplo de exploit (campo password):
```
1234' OR 1=1 --
```
o
```
x' OR 5=5
```

Cómo probar:
1. Inicia la API: `uvicorn app.main:app --reload`.
2. Abre `login_demo.html` en tu navegador (doble clic o Live Server).
3. Ingresa un usuario cualquiera y en contraseña un payload como arriba.
4. Pulsa "Login Inseguro" para ver que la tautología devuelve filas y "loguea".
5. Pulsa "Login Seguro": no debería autenticar salvo credenciales reales (`gaston` / `1234`).

Respuesta del endpoint inseguro incluye la query construida y los registros obtenidos.

IMPORTANTE: Este código vulnerable es solo para aprendizaje. En producción:
- Usar siempre parámetros (prepared statements / ORM).
- No revelar la query cruda en la respuesta.
- Almacenar contraseñas con hashing seguro (bcrypt, argon2).
- Aplicar principios de mínimo privilegio y validación estricta de entrada.

## Configuración
- Variables por defecto en `app/config.py`.
- Cambia la URL de la base de datos con la variable de entorno `DATABASE_URL` (archivo `.env` si lo deseas).

## Próximos pasos
- Modelar entidades según el UML proporcionado.
- Crear rutas CRUD y relaciones (SQLModel) usando SQLite.
- Añadir pruebas y validación.
