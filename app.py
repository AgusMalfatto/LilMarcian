from flask import Flask, render_template, request, redirect, url_for
from controlador import connect as cnt

app = Flask(__name__)

# HomePage
@app.route('/', methods=['GET', 'POST'])
def home():
    stock_data = cnt.get_stock()
    
    return render_template("index.html", stock_data=stock_data, name="Apple")

# Login
@app.route("/login")
def login():
    return render_template("sesion/login.html")

# Register
@app.route("/register")
def register():
    return render_template("sesion/register.html") 

@app.route("/search", methods=['POST'])
def search_stock():
    stock = request.form['stock-search']
    stock_data = cnt.get_stock(stock)
    return render_template("index.html", stock_data=stock_data, name=stock)

# Start App
if __name__ == '__main__':
    app.run(debug=True)