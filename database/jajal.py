import mysql.connector


MyDB = mysql.connector.connect(
    # menghubungkan program dengan database MySQL
    # set host, user, password, database
    host = "localhost",
    user = "root",
    password = "admin",
    database = "barang",
)
