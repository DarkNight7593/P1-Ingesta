# Imagen base minimalista de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /ingesta

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    python3-dev \
    curl \
    && pip install --upgrade pip \
    && pip install boto3 mysql-connector-python pandas python-dotenv \
    && apt-get remove -y gcc python3-dev \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copiar los archivos del proyecto al contenedor
COPY . .

# Ejecutar el script principal
CMD ["python3", "myseq.py"]
