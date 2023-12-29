import psycopg2
from dotenv import dotenv_values

config = dotenv_values(".env") 
conn = psycopg2.connect(database=config["POSTGRES_DB"],
                        host=config["POSTGRES_HOST"],
                        user=config["POSTGRES_USER"],
                        password=config["POSTGRES_PASSWORD"],
                        port=config["POSTGRES_PORT"])
