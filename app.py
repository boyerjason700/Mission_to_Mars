# Use Flask to render a template, redirecting to another url, and creating a URL.
# Use PyMongo to interact with our Mongo database.
# Use the scraping code, we will convert from Jupyter notebook to Python


from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

# Setup flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
# db = client.mars_app
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Define route for HTML page
@app.route("/")
def index():
    # Uses PyMongo to find the "mars" collection in our database
   mars = mongo.db.mars.find_one()
   # Flask to return HTML template using an index.html file, 'mars=mars' tell Python to use 'mars' collection in mongoDB
   return render_template("index.html", mars=mars)

# Scrape route
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)

# tell flask to run
if __name__ == "__main__":
   app.run()