from os import environ
from dotenv import load_dotenv

load_dotenv()

CONNECT_STR = environ.get('CONNECT_STR')
