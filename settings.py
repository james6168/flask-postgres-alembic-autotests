from os import getenv
from dotenv import load_dotenv

load_dotenv()

FLASK_APP_API_URL = getenv("FLASK_APP_API_URL")
