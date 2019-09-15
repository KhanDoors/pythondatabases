import psycopg2


def connect():
    return psycopg2.connect(user='postgres', password='syyad', database='learning', host='localhost')