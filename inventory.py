import sqlite3

# Connect to database
connection = sqlite3.connect("inventory.db")

# Create cursor
cursor = connection.cursor()

# Create Table
cursor.execute(""" CREATE TABLE inventory (
                Product text,
                On_hand integer,
                Missing intege
            )""")

    
PRODUCTS = [
    ("Product", "On_hand", "Missing"),
    ("Chicken", 10, 0),
    ("Beef", 10, 0),
    ("Lamb", 10, 0),
    ("Carrots", 10, 0),
    ("Green Beans", 10, 0),
    ("Brocoli", 10, 0),
    ("Potatoes", 10, 0),
    ("Squash", 10, 0)
]

cursor.executemany("insert into inventory values (?,?,?)", PRODUCTS)

# Commit our command
connection.commit()

#shows the whole data base
"""for row in cursor.execute("select * from inventory"):
    print(row)"""

cursor.execute("select * from inventory where On_hand=:out", {"out": "0"})
OutofStock_Search = cursor.fetchall()
print(OutofStock_Search)

connection.close()
