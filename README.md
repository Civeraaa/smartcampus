
# SmartCampus

API REST para la gestión de espacios y reservas de un campus universitario. El proyecto está desarrollado en Python y organizado en módulos para separar la aplicación, los modelos y la lógica de servicios.

## Estructura del proyecto

```text
smartcampus/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   └── services.py
├── tests/
│   ├── test_bookings.py
│   ├── test_rooms.py
│   └── test_services.py
├── .github/
│   └── workflows/
├── .githooks/
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Requisitos

- Python 3.11 o superior
- Git
- Docker Desktop y Docker Compose (para ejecutar con contenedores)

## Instalación y ejecución local

Clonar el repositorio:

```bash
git clone https://github.com/Civeraaa/smartcampus.git
cd smartcampus
```

Crear y activar un entorno virtual:

```bash
python -m venv .venv
```

En Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Crear el archivo de configuración local a partir del ejemplo:

```powershell
Copy-Item .env.example .env
```

Iniciar la aplicación:

```bash
uvicorn app.main:app --reload
```

La API estará disponible localmente en `http://127.0.0.1:8000`.

## Ejecución con Docker

Construir y arrancar los servicios:

```bash
docker compose up -d --build
```

Consultar los contenedores:

```bash
docker compose ps
```

Ver los registros:

```bash
docker compose logs -f
```

Detener los servicios:

```bash
docker compose down
```

## Tests

Ejecutar la suite de pruebas con pytest:

```bash
pytest -v
```

Los tests cubren las funcionalidades relacionadas con reservas, salas y servicios.

## Git hooks

El proyecto incluye hooks de Git para automatizar comprobaciones y acciones durante el flujo de trabajo. Los hooks disponibles son:

- `pre-commit`
- `post-commit`
- `pre-push`
- `post-push`

Consulta los scripts incluidos en el repositorio para conocer las acciones que realiza cada hook.

## Integración continua y despliegue

El proyecto utiliza GitHub Actions para automatizar el proceso de integración y despliegue.

El flujo incluye:

- Ejecución de tests en una matriz de versiones de Python.
- Construcción de la imagen Docker.
- Despliegue automático condicionado a los cambios en la rama principal.
- Uso de variables y secretos configurados en GitHub Actions para la configuración del despliegue.

## Configuración

El archivo `.env.example` contiene una plantilla de las variables de entorno necesarias. Para la ejecución local, se debe crear un archivo `.env` a partir de esta plantilla.

Los valores sensibles no deben subirse al repositorio. En GitHub Actions, los secretos se configuran desde **Settings → Secrets and variables → Actions**.

## Repositorio

[https://github.com/Civeraaa/smartcampus](https://github.com/Civeraaa/smartcampus)
