from dotenv import load_dotenv
from os import environ

SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL")

ARTICLES_PER_PAGE = 4

load_dotenv()
