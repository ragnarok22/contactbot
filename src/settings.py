import os

import dotenv

dotenv.load_dotenv()

TELEGRAM_KEY = os.getenv('TELEGRAM_KEY')
CLEARDB_DATABASE_URL = os.getenv('CLEARDB_DATABASE_URL')
