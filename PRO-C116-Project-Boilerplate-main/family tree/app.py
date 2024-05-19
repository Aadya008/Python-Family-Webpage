# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Aadya" # write your name
    age = "14" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def second_flask():

    name = "Rajiv" # write your name
    age = "42" # write your age

# define the route to mother webpage
@app.route("/mother")
def third_flask():

    name= "Shambhavi" # write your name
    age = "39" # write your age

# define the route to sister webpage
@app.route("/sister")
def fourth_flask():

    name = "Advita" # write your name
    age = "8" # write your age

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
