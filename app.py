from potatomanager import PotatoManager
from flask import Flask, render_template, redirect, request

app = Flask(__name__)
potatomanager = PotatoManager()

@app.route("/")
def get_all_articles():
    return render_template('home.html', potatos=potatomanager.get_all())

@app.route("/create", methods=["POST"])
def create_potato():
    potato, stock = request.json.get('potato'), request.json.get('stock')
    potatomanager.set(potato=potato, stock=stock)
    return redirect('/')

@app.route("/add", methods=["POST"])
def add_potato():
    potato, amt_to_add = request.json.get('potato'), request.json.get('amt_to_add')
    potatomanager.add(potato=potato, amt_to_add=amt_to_add)
    return redirect('/')

@app.route("/remove", methods=["POST"])
def remove_potato():
    potato, amt_to_remove = request.json.get('potato'), request.json.get('amt_to_remove')
    potatomanager.remove(potato=potato, amt_to_remove=amt_to_remove)
    return redirect('/')

@app.route("/supplierconnect")
def connect_supplier():
    potatomanager.supplierconnect()
    return redirect('/')


if __name__ == '__main__':
    app.run('0.0.0.0', 1369)