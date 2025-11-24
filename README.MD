# Lince - Backend Django

Proyecto backend desarrollado con Django y Django REST Framework, containerizado con Docker para facilitar el desarrollo y despliegue.

## Tecnologías

- **Django 5.2.7** - Framework web
- **Django REST Framework 3.16.1** - API REST
- **PostgreSQL 15** - Base de datos
- **Docker & Docker Compose** - Containerización

## Requisitos Previos

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado y corriendo
- Git

## Instalación y Configuración

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd Lince/Lince
```

### 2. Levantar el proyecto con Docker

```bash
docker-compose up -d
```

Este comando:
- Construye las imágenes de Docker
- Inicia PostgreSQL
- Inicia Django
- Ejecuta las migraciones automáticamente
- Levanta el servidor en `http://localhost:8000`

**Espera ~10-15 segundos** la primera vez mientras se construyen las imágenes y se ejecutan las migraciones.

### 3. Verificar que todo esté corriendo

```bash
docker-compose ps
```

Deberías ver dos contenedores corriendo:
- `postgres_django` - Base de datos PostgreSQL
- `django_web` - Aplicación Django

## Uso

### Acceder a la aplicación

- **API**: http://localhost:8000/api
- **Admin**: http://localhost:8000/admin (requiere crear superusuario)

### Crear un superusuario

```bash
docker-compose exec web python manage.py createsuperuser
```

### Detener el proyecto

```bash
docker-compose down
```

**Nota:** Tus datos se mantienen guardados. Para eliminar también los datos:

```bash
docker-compose down -v  #  Esto borra la base de datos, ten cuidado
```

## Comandos Útiles

### Gestión de Django

```bash
# Crear migraciones
docker-compose exec web python manage.py makemigrations

# Aplicar migraciones
docker-compose exec web python manage.py migrate

# Abrir shell de Django
docker-compose exec web python manage.py shell

# Ejecutar tests
docker-compose exec web python manage.py test
```

### Ver logs

```bash
# Ver logs de Django
docker-compose logs web

# Ver logs en tiempo real
docker-compose logs -f web

# Ver logs de PostgreSQL
docker-compose logs db
```

### Reconstruir contenedores

```bash
# Si modificas Dockerfile o requirements.txt
docker-compose build

# Reconstruir y reiniciar
docker-compose up -d --build
```

### Acceder a la base de datos

```bash
docker-compose exec db psql -U django_user -d django_db
```

## Desarrollo

Los cambios en el código se reflejan automáticamente gracias al volumen montado. No necesitas reconstruir el contenedor para ver cambios en Python.

**Solo necesitas reconstruir si modificas:**
- `requirements.txt`
- `Dockerfile`
- `entrypoint.sh`

## Estructura del Proyecto

```
Lince/
├── Lince/              # Configuración del proyecto Django
├── api/                # Aplicación API
├── Dockerfile          # Configuración del contenedor Django
├── docker-compose.yml  # Orquestación de contenedores
├── entrypoint.sh       # Script de inicialización
├── requirements.txt    # Dependencias Python
└── manage.py           # CLI de Django
```

## Troubleshooting

### Los contenedores no inician

```bash
# Ver logs de errores
docker-compose logs

# Reconstruir desde cero
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

### Error de conexión a la base de datos

```bash
# Reiniciar solo el contenedor de Django
docker-compose restart web
```

### Resetear todo (base de datos incluida)

```bash
docker-compose down -v
docker-compose up -d
```

## Notas

- Los datos de PostgreSQL persisten entre reinicios en el volumen `postgres_data`
- El servidor de desarrollo corre en modo debug (`DEBUG=True`)
- Para producción, se recomienda usar Gunicorn/uWSGI y configurar variables de entorno apropiadas
- Este archivo se irá actualizando conforme se vaya avanzando en el proyecto