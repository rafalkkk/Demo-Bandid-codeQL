import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

name = input("Enter name: ")
age = input("Enter age: ")

query = f"SELECT * FROM users WHERE name = '{name}' AND age = {age}"
c.execute(query)
result = c.fetchone()

if result:
    print("User found")
else:
    print("User not found")
