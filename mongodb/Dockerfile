FROM python:3.9-slim

# Crear directorio de trabajo
WORKDIR /ingesta

# Instalar dependencias necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && python -m pip install --no-cache-dir --upgrade pip \
    && python -m pip install --no-cache-dir boto3 pymongo python-dotenv \
    && apt-get remove -y gcc \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# Copiar archivos al contenedor
COPY . .

# Comando por defecto
CMD ["python", "mongo.py"]
