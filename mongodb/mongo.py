import json
import boto3
from pymongo import MongoClient
import os
from datetime import datetime
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Función para convertir datetime a string
def convert_datetime(o):
    if isinstance(o, datetime):
        return o.isoformat()
    raise TypeError(f'Object of type {o.__class__.__name__} is not JSON serializable')

# Verificación de variables de entorno necesarias
required_env_vars = ['MONGO_USER', 'MONGO_PASSWORD', 'HOST', 'MONGO_PORT', 'S3_BUCKET']
missing_vars = [var for var in required_env_vars if not os.getenv(var)]

if missing_vars:
    raise EnvironmentError(f"❌ Las siguientes variables de entorno faltan: {', '.join(missing_vars)}")

# Conexión a MongoDB
try:
    mongo_uri = f"mongodb://{os.getenv('MONGO_USER')}:{os.getenv('MONGO_PASSWORD')}@{os.getenv('HOST')}:{os.getenv('MONGO_PORT')}/"
    mongo_client = MongoClient(mongo_uri)
    db = mongo_client['hospital']
    collection = db['Pacientes']
    mongo_client.server_info()  # Verifica la conexión
    print("✅ Conexión exitosa a MongoDB")
except Exception as e:
    print(f"❌ Error al conectar a MongoDB: {e}")
    mongo_client = None

# Exportar documentos y subir a S3
if mongo_client:
    output_file = 'ingesta_pacientes.json'
    try:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for document in collection.find():
                document = json.loads(json.dumps(document, default=convert_datetime))
                outfile.write(json.dumps(document) + "\n")
        print(f"📄 Datos exportados a {output_file}")
    except Exception as e:
        print(f"❌ Error al exportar datos a JSON: {e}")
        exit(1)

    # Subida a S3
    try:
        s3_client = boto3.client('s3')
        bucket_name = os.getenv('S3_BUCKET')
        s3_file_name = 'ing_pacientes/pacientes.json'
        s3_client.upload_file(output_file, bucket_name, s3_file_name)
        print(f"✅ Archivo subido a S3: s3://{bucket_name}/{s3_file_name}")
    except Exception as e:
        print(f"❌ Error al subir a S3: {e}")
