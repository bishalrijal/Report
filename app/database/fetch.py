import mysql.connector
from database import setup

def getUser():
    mydb = mysql.connector.connect(host=setup.SOURCE_DB['host'],
                        user=setup.SOURCE_DB['name'],
                        passwd=setup.SOURCE_DB['password'],
                         database=setup.SOURCE_DB['database'])
    mycursor = mydb.cursor()
    mycursor.execute('SELECT id,username,email,is_active,created_at FROM users')
    columns = [ field[0] for field in mycursor.description]
    result = mycursor.fetchall()
    mydb.close()
    return (columns,result)

