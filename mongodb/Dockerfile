# Imagen base ligera con Python 3.9
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Instalar solo las dependencias necesarias sin limpiar nada
RUN apt-get update && \
    apt-get install -y gcc libpq-dev && \
    pip install boto3 pymongo python-dotenv

# Copiar los archivos del proyecto
COPY . .

# Comando por defecto
CMD ["python3", "mongo.py"]



