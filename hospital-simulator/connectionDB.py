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

def create_entities(table, id, name=None):
    cnx = mysql()
    cursor = cnx.cursor()
    insert = ("INSERT INTO {} ").format(table)
    params = ''
    values = ''
    if name==None:
        query = (insert + "(id) VALUES (%s)" % (id))
        cursor.execute(query)
    else:
        params = ("(id, nombre)")
        values = ("(%s, %s)")
        query = (insert + params +" VALUES "+ values)
        cursor.execute(query, (id, name))

    # print(query, data)
    cnx.commit()
    cursor.close()
    cnx.close()

def truncate_tables():
    cnx = mysql()
    cursor = cnx.cursor()

    cursor.execute('SET FOREIGN_KEY_CHECKS=0')
    cursor.execute('TRUNCATE TABLE simulacion')
    cursor.execute('TRUNCATE TABLE registros_du')
    cursor.execute('TRUNCATE TABLE registros_sr')
    cursor.execute('TRUNCATE TABLE registros_e')
    cursor.execute('TRUNCATE TABLE hospital_ingreso')
    cursor.execute('TRUNCATE TABLE registros_hi')
    cursor.execute('TRUNCATE TABLE registros_da')
    cursor.execute('TRUNCATE TABLE registros_r')
    cursor.execute('TRUNCATE TABLE espera')
    cursor.execute('TRUNCATE TABLE doctores_admision')
    cursor.execute('TRUNCATE TABLE pacientes')
    cursor.execute('TRUNCATE TABLE sala_radiografia')
    cursor.execute('TRUNCATE TABLE doctores_urgencias')
    cursor.execute('TRUNCATE TABLE radiografia')
    cursor.execute('TRUNCATE TABLE enfermeras')
    # cursor.execute('SET FOREIGN_KEY_CHECKS=1')

    cnx.commit()
    cursor.close()
    cnx.close()
