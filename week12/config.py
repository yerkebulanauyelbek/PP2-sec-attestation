import psycopg2
config = psycopg2.connect(
    host="localhost",
    database="suppliers",
    user="postgres",
    password="excel2002" 
)