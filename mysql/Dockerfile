# Imagen base ligera con Python 3.9
FROM python:3.9-slim

# Establecer directorio de trabajo
WORKDIR /app

# Instalar dependencias necesarias sin eliminar nada
RUN apt-get update && \
    apt-get install -y gcc libmariadb-dev && \
    pip install mysql-connector-python pandas boto3 python-dotenv

# Copiar los archivos del proyecto
COPY . .

# Comando por defecto al iniciar el contenedor
CMD ["python3", "myseq.py"]
