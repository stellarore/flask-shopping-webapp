import sqlite3

groceries = []
with open("groceries_import.csv") as f:
    for line in f:
        if line[0] != "#":
            groceries.append(line.rstrip().split(','))

conn = sqlite3.connect("grocerylist.db")
cursor = conn.cursor()

for groc in groceries:
    # departments:
    # produce = 1-Produce
    # bakery = 2-Bakery
    # meat = 3-Meat
    # soda = 4-Soda
    # snacks = 5-Snacks
    # dry = 6-DryGoods
    # misc = 7-Misc
    # froz = 8-Frozen
    # dairy = 9-Dairy
    conv = {'produce':'1-Produce',
            'bakery':'2-Bakery',
            'meat':'3-Meat',
            'soda':'4-Soda',
            'snacks':'5-Snacks',
            'dry':'6-DryGoods',
            'misc':'7-Misc',
            'froz':'8-Frozen',
            'dairy':'9-Dairy'}

    # print(groc[0],1,conv[groc[1]])

    cursor.execute("INSERT INTO groceries (item, number, department) VALUES (?,?,?)", [groc[0],1,conv[groc[1]]])

conn.commit()
conn.close()
print('finish')
