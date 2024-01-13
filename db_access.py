import mysql.connector

conn=mysql.connector.connect(host='localhost',password='Onlinemedia#@!',user='root')
if conn.is_connected():
    print("Connection established.....")
try:
    cursor=conn.cursor()
    cursor.execute('SELECT * FROM siddhudb1.employee')
    results=cursor.fetchall()

    for result in results:
        print(f"Data retrieved from DB is: {result} ")
except mysql.connector.errors as err:
    print(f"Error: {err}")

conn.rollback()
