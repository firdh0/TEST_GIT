import sqlalchemy
from dotenv import load_dotenv
import os

load_dotenv()

password = os.getenv("DB_PASSWORD")
username = os.getenv("DB_USERNAME")