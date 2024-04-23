import os
from dotenv import load_dotenv

dotenv_path = '/home/cirodirosa0/career_site/.env'
load_dotenv(dotenv_path)

secret_key = os.getenv("SECRET_KEY")
print(secret_key)