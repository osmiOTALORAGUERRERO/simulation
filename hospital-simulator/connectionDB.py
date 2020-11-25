from mysql import connector
from mysql.connector import Error
from global_var import passwordDB

def mysql():
    try:
        cnx = connector.connect(
            user='root',
            password=passwordDB,
            host='127.0.0.1',
            database='hospital_simulator'
        )
        print('connectionDB stablished')
        return cnx
    except Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
        exit()
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
        exit()
      else:
        print(err)
        exit()
    else:
        cnx.close()
        exit()
