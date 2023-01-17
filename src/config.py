from decouple import config

user = config('PGSQL_USER')
password = config('PGSQL_PASSWORD')
host = config('PGSQL_HOST')
database = config('PGSQL_DATABASE')

secret_key = config('SECRET_KEY')

DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{user}:{password}@{host}/{database}'