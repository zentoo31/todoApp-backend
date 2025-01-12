from dotenv import load_dotenv
import os

load_dotenv()

DB_STR = os.getenv("DB_STR")
DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")