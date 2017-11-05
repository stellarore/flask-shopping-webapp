from flask import Flask, render_template
from flask import request, redirect
from flask import g
import sqlite3
app = Flask(__name__)


@app.before_request
def before_request():
    g.db = sqlite3.connect("grocerylist.db")


@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

@app.route('/')
def index():
    grocery_list = g.db.execute("SELECT * FROM groceries ORDER BY department ASC").fetchall()
    to_buy = []
    bought = []
    for i in grocery_list:
        if i[1] > 0: to_buy.append(i)
        else: bought.append(i)
    # where number > 0
    # separate list where number = 0
    # separate button to save checkoffs
    return render_template('index.html', grocery_list=to_buy, bought_list=bought)

@app.route('/checkoffItem', methods=['POST'])
def checkoff():
    item_name = request.form['item_name']
    g.db.execute("UPDATE groceries SET number=0 WHERE item='{}'".format(item_name))
    g.db.commit()
    return redirect('/')

@app.route('/checkonItem', methods=['POST'])
def checkon():
    item_name = request.form['item_name']
    g.db.execute("UPDATE groceries SET number=1 WHERE item='{}'".format(item_name))
    g.db.commit()
    return redirect('/')


@app.route('/addItem', methods = ['POST'])
def addItem():
    item_name = request.form['item_name']
    number = request.form['item_number']
    department = request.form['department']

    g.db.execute("INSERT INTO groceries (item, number, department) VALUES (?,?,?)", [item_name, number, department])
    g.db.commit()

    print("Added: {},{},{}".format(item_name, number, department))
    return redirect('/')

@app.route('/addOne', methods=['POST'])
def addOne():
    item_name = request.form['item_name']
    item_number = str(int(request.form['item_number']) + 1)
    g.db.execute("UPDATE groceries SET number={} WHERE item='{}'".format(item_number, item_name))
    g.db.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run()