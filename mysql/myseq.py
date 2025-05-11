import os
import mysql.connector
import pandas as pd
import boto3
from mysql.connector import Error
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Validación de variables necesarias
required_vars = ['HOST', 'MYSQL_USER', 'MYSQL_PASSWORD', 'MYSQL_DATABASE', 'MYSQL_PORT', 'S3_BUCKET']
for var in required_vars:
    if not os.getenv(var):
        raise EnvironmentError(f"La variable de entorno requerida '{var}' no está definida.")

# Tablas fijas a exportar
tables_to_export = ['historias_clinicas', 'cita']

try:
    # Conexión a MySQL
    conn = mysql.connector.connect(
        host=os.getenv('HOST'),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        database=os.getenv('MYSQL_DATABASE'),
        port=os.getenv('MYSQL_PORT'),
        auth_plugin='mysql_native_password'
    )

    if conn.is_connected():
        print("✅ Conectado a MySQL.")
        s3_client = boto3.client('s3')
        bucket_name = os.getenv('S3_BUCKET')

        for table in tables_to_export:
            # Leer tabla en un DataFrame
            df = pd.read_sql(f"SELECT * FROM {table}", con=conn)

            # Guardar como CSV
            file_name = f"{table}_dump.csv"
            df.to_csv(file_name, index=False)

            # Subir a S3
            s3_key = f"ing_historias/{table}.csv"
            s3_client.upload_file(file_name, bucket_name, s3_key)
            print(f"📤 '{file_name}' exportado exitosamente a S3 en '{s3_key}'.")

except Error as e:
    print(f"❌ Error de conexión a MySQL: {e}")

except Exception as e:
    print(f"❌ Error general: {e}")

finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("🔒 Conexión a MySQL cerrada.")
