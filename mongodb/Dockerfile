FROM python:3.9-slim

# Establecer directorio de trabajo
WORKDIR /ingesta

# Instalar dependencias necesarias en un solo paso
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*  # Limpiar la cache de apt para reducir el tamaño de la imagen

# Instalar las dependencias de Python
RUN pip install --no-cache-dir --upgrade pip boto3 psycopg2-binary pandas python-dotenv

# Copiar los archivos de la aplicación (si es necesario)
COPY . .

# Establecer el comando predeterminado para ejecutar tu aplicación (si es necesario)
CMD ["python", "app.py"]

