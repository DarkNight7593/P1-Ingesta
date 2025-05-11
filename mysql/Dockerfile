# Imagen base minimalista de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /ingesta

# Instalar dependencias del sistema necesarias y luego limpiar
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    python3-dev \
    curl \
    && pip install --upgrade pip \
    && pip install --no-cache-dir boto3 mysql-connector-python pandas python-dotenv \
    && apt-get purge -y --auto-remove gcc python3-dev \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Copiar los archivos del proyecto al contenedor
COPY . .

# Ejecutar el script principal
CMD ["python3", "myseq.py"]

