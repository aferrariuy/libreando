#!/bin/bash
set -e

echo "Configurando variables de entorno del frontend..."

# Asegurar que PUBLIC_API_BASE_URL esté disponible para el build
export PUBLIC_API_BASE_URL=${PUBLIC_API_BASE_URL:-http://localhost:8000}

# Crear archivo .env para el frontend con variables de Render
cat > frontend/.env << EOF
PUBLIC_API_BASE_URL=${PUBLIC_API_BASE_URL}
EOF

echo "PUBLIC_API_BASE_URL configurado como: ${PUBLIC_API_BASE_URL}"

echo "Reconstruyendo frontend con variables de entorno..."
cd frontend
npm install

# Construir con la variable de entorno disponible
PUBLIC_API_BASE_URL=${PUBLIC_API_BASE_URL} npm run build
cd ..

echo "Esperando a que la base de datos esté lista..."
python -c "
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'libreando.settings')
django.setup()
from django.db import connection
from django.db.utils import OperationalError
import time
for i in range(30):
    try:
        connection.ensure_connection()
        break
    except OperationalError:
        time.sleep(1)
else:
    raise Exception('Database did not become available')
print('Database is ready!')
"

echo "Ejecutando migraciones..."
python manage.py migrate

echo "Recolectando archivos estáticos..."
python manage.py collectstatic --noinput

echo "Creando superusuario si no existe..."
python manage.py shell -c "exec(open('create_admin.py').read())" || true

echo "Iniciando servidor..."
exec gunicorn --bind 0.0.0.0:8000 --workers 3 --timeout 120 libreando.wsgi:application