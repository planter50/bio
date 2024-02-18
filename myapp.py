
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
 
app = Flask(__name__) 
  
# Pass the required route to the decorator. 
@app.route("/contact") 
def contact1(): 
    #return "Hello, welcome to cyberebels! Checkout https:cyberebels.com/aboutus to see more"
    return render_template('contact.html')

@app.route('/aboutus')
def index():
    #return "Meet the team!"
    return render_template('aboutus.html')
    
@app.route("/") 
def mainpage1(): 
    #return "Homepage of GeeksForGeeks"
    return render_template('mainpage.html')
@app.route("/services")
def services1(): 
    return render_template('services.html')
    #return "work in progress"
@app.route("/") 
def hello(): 
    #return "Hello, Welcome to GeeksForGeeks"
    return render_template('first.html')
@app.route("/store")
def store(): 
    return render_template('store.html')

@app.route("/countdown")
def countdown():
    return render_template('countdown.html')  
    #return "hello"

@app.route("/planter500")
def planter():
	return render_template("/planter500.html")

@app.route("/one")
def once():
    return render_template('/one.html')

if __name__ == "__main__": 
    app.run(debug=True) 


