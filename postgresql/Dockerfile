# Imagen base ligera con Python 3.9
FROM python:3.9-slim

# Establecer directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalar dependencias del sistema necesarias para psycopg2 y limpiar caché
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev && \
    pip install --no-cache-dir boto3 psycopg2-binary pandas python-dotenv && \
    apt-get purge -y gcc && \
    apt-get autoremove -y && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copiar los archivos del proyecto
COPY . .

# Comando por defecto al iniciar el contenedor
CMD ["python3", "postgres.py"]
