from config import config
cursor = config.cursor()

def create_table():
    creating_table = """
    CREATE TABLE population(
    name VARCHAR(20),
    surname VARCHAR(20),
    age INTEGER,
    city VARCHAR(20)
    )
    """
    cursor.execute(creating_table)
    config.commit()


def insert(name, surname, age, city):
    cursor.execute(f"INSERT INTO population VALUES('{name}', '{surname}', {age}, '{city}')")
    config.commit()


def update():
    cursor.execute(f"UPDATE population SET surname = '' WHERE name = ''")
    config.commit()

def queue():
    cursor.execute(f"SELECT * FROM population")
    data = cursor.fetchall()
    return data

def delete():
    cursor.execute(f"DELETE FROM population WHERE name = ''")
    config.commit()
