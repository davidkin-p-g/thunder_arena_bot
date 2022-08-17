from platform import python_branch
from mysql.connector import MySQLConnection
from mysql.connector import Error

from python_mysql_dbconfig import read_db_config

# Проверка подключения
def _connection():
    db_config = read_db_config()
    try:
        conn = MySQLConnection(**db_config)
        if conn.is_connected():
            print('connection established.')
        else:
            print('connection failed.')
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        conn.close()
        print('Connection closed.')

    return conn

# Отправка запроса
def execute_query(exec_name, argx = None):
    try:
        # Проверяем кофиг и подключаемся к базе
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        # Вызываем хранимую процедуру
        if argx == None:
            cursor.callproc(exec_name)
        else:
            cursor.callproc(exec_name, argx)
        conn.commit()
        return cursor.stored_results()
    except Error as e:
        return(f"error '{e}' occurred")
    
    finally:
        cursor.close()
        conn.close()