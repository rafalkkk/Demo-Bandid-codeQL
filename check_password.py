import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

username = input("Enter username: ")
password = input("Enter password: ")

# query1 = f"SELECT * FROM users WHERE name = '{username}' AND password = '{password}'"

# print(f'User validation with {query1}')
# c.execute(query1)
# result = c.fetchone()

# if result:
#     print("Login successful")
# else:
#     print("Login failed")


query2 = f"SELECT * FROM users WHERE name = ? AND password = ?"
print(f'User validation with {query2}')
c.execute(query2, (username, password))

# lets correct it!
#c.execute("SELECT * FROM users WHERE name = ? AND password = ?", (username, password))
result = c.fetchone()

if result:
    print("Login successful")
else:
    print("Login failed")

        