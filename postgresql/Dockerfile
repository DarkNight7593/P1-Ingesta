# Imagen base ligera con Python 3.9
FROM python:3.9-slim

# Establecer directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema necesarias para psycopg2
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev

# Instalar dependencias de Python necesarias
RUN pip install --no-cache-dir psycopg2-binary pandas boto3

# Copiar archivos del proyecto
COPY . .

# Comando por defecto
CMD ["python3", "postgres.py"]


