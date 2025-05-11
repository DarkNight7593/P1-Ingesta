import os
import psycopg2
import boto3
import pandas as pd

# ------------------ Verificación de variables de entorno ------------------
REQUIRED_ENV_VARS = [
    'PG_DB', 'PG_USER', 'PG_PASSWORD', 'HOST', 'PG_PORT',
    'S3_BUCKET'
]

missing_vars = [var for var in REQUIRED_ENV_VARS if not os.getenv(var)]
if missing_vars:
    raise EnvironmentError(f"Faltan variables de entorno requeridas: {', '.join(missing_vars)}")

# ------------------ Conexión a PostgreSQL ------------------
try:
    print("📡 Conectando a PostgreSQL...")
    connection = psycopg2.connect(
        database=os.getenv('PG_DB'),
        user=os.getenv('PG_USER'),
        password=os.getenv('PG_PASSWORD'),
        host=os.getenv('HOST'),
        port=os.getenv('PG_PORT')
    )
    print("✅ Conectado a PostgreSQL")
except psycopg2.Error as e:
    print(f"❌ Error al conectar a PostgreSQL: {e}")
    exit(1)

# ------------------ Exportar tablas específicas ------------------
try:
    s3 = boto3.client('s3')
    bucket = os.getenv('S3_BUCKET')

    tablas = ['Doctor', 'Disponibilidad']
    for tabla in tablas:
        print(f"📤 Exportando tabla: {tabla}")
        df = pd.read_sql(f"SELECT * FROM {tabla}", con=connection)

        # Guardar CSV localmente
        archivo_local = f"{tabla}.csv"
        df.to_csv(archivo_local, index=False, header=True)

        # Ruta destino en S3
        archivo_s3 = f"ing_doctores/{tabla}.csv"

        # Subir a S3
        s3.upload_file(archivo_local, bucket, archivo_s3)
        print(f"✅ {tabla} exportada a S3 en '{archivo_s3}'")

except Exception as e:
    print(f"❌ Error durante la exportación: {e}")

finally:
    if connection:
        connection.close()
        print("🔒 Conexión a PostgreSQL cerrada.")
