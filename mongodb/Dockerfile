# Imagen base ligera con Python 3.9
FROM python:3.9-slim

# Establecer directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalar dependencias necesarias
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev && \
    pip install --no-cache-dir boto3 pymongo python-dotenv && \
    apt-get purge -y gcc && \
    apt-get autoremove -y

# Copiar los archivos del proyecto
COPY . .

# Comando por defecto al iniciar el contenedor
CMD ["python3", "mongo.py"]


