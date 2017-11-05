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
    grocery_list = g.db.execute("SELECT * FROM groceries").fetchall()
    return render_template('index.html', grocery_list=grocery_list)

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/addItem', methods = ['POST'])
def addItem():
    item_name = request.form['item_name']
    number = request.form['item_number']
    department = request.form['department']

    g.db.execute("INSERT INTO groceries (item, number, department) VALUES (?,?,?)", [item_name, number, department])
    g.db.commit()

    print("Added: {},{},{}".format(item_name, number, department))
    return redirect('/')

if __name__ == '__main__':
    app.run()