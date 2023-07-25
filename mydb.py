import mysql.connector
dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='WakeUp23#@!'
)
cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE maryas")
print("good job")