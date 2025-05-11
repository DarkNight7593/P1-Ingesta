# Imagen base ligera con Python 3.9
FROM python:3.9-slim

# Establecer directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema necesarias para mysql-connector y pandas
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libmariadb-dev && \
    pip install --no-cache-dir mysql-connector-python pandas boto3 python-dotenv && \
    apt-get purge -y gcc && \
    apt-get autoremove -y

# Copiar los archivos del proyecto
COPY . .

# Comando por defecto al iniciar el contenedor
CMD ["python3", "mysql.py"]

