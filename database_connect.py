import mysql.connector as connector

def connect():
    return connector.connect(host='localhost',user='root',password='ibrahim',database='travels')