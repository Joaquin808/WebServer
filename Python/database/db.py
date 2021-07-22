import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


# def create_connection():
#     conn = psycopg2.connect(dbname="postgres",
#                             user="kin", host="",
#                             password="youngskater")
#
#     conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
#
#     cursor = conn.cursor()
#
#     cursor.execute(sql.SQL("CREATE DATABASE mydatabase"))
#
#     return conn
#
#
# connection = create_connection()
