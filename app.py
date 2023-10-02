from flask import Flask, render_template, request, redirect, url_for
from framework.Stock import Stock

app = Flask(__name__)

stock = Stock()

# HomePage
@app.route('/', methods=['GET', 'POST'])
def home():
    stock_data = stock.get_stock_json()
    
    return render_template("index.html", stock_data=stock_data, name="Apple")

# Login
@app.route("/login")
def login():
    return render_template("sesion/login.html")

# Register
@app.route("/register")
def register():
    return render_template("sesion/register.html") 

# Search Stock
@app.route("/search", methods=['POST'])
def search_stock():
    stock_search = request.form['stock-search']
    stock.symbol = stock_search
    stock_data = stock.get_stock_json()
    return render_template("index.html", stock_data=stock_data, name=stock.symbol)



# Start App
if __name__ == '__main__':
    app.run(debug=True)