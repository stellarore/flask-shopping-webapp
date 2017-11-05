import sqlite3

groceries = []
with open("groceries_import.csv") as f:
    for line in f:
        if line[0] != "#":
            groceries.append(line.rstrip().split(','))

for i in range(5):
    print(groceries[i])





# conn = sqlite3.connect("grocerylist.db")
#
# cursor = conn.cursor()
#
# cursor.execute("ADD")
#
#
#
#
#
# conn.commit()
# conn.close()
