from mysql.connector import Error
from config import dataBase

def testConnect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = dataBase.DB
        if conn.is_connected():
            print('Connected to MySQL database')
            return True

    except Error as e:
        print(e)
        return False