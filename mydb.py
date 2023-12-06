import mysql.connector

db= mysql.connector.connect(
    host="localhost",
    user='root',
    passwd='Password123',
    auth_plugin='mysql_native_password',
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE elderco")

print("Database İşlemleri Başarılı")
