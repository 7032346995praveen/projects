
import mysql.connector as sql
import pandas as pd

db_connection = sql.connect(host='localhost',database='sakila',user='root',password='123456')
db_cursor = db_connection.cursor()
db_cursor.execute('select address from sakila.address')
address = db_cursor.fetchall()
df=pd.DataFrame(address)
print(df)
