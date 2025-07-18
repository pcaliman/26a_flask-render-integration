from waitress import serve
from app import app

import os

port = int(os.environ.get("PORT", 5000))  # Leer el puerto de Railway
serve(app, host='0.0.0.0', port=port)
