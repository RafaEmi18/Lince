
## Pasos para levantar el proyecto

Sigue estos pasos para poner en marcha el proyecto en tu entorno local.

### 1. Clonar el repositorio

### 2. Crear un entorno virtual

```bash
python -m venv .venv
.venv\Scripts\activate  # iniciar entorno virtual en Windows
source .venv/bin/activate  #iniciar entorno virtual en Linux/Mac
```



### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Levantar base de datos MySQL
```bash
docker-compose up -d
```

### 5. Levantar proyecto
```bash
python manage.py migrate
python manage.py runserver

```
### 6. Enpoints 

Endpoints disponibles en: \
http://127.0.0.1:8000/api

