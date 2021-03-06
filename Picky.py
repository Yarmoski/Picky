from flask import Flask, render_template, flash, url_for, redirect
from flask import request as flask_request #This alias is used because Yelp contains a function "request"
from Yelp import *
import os

app = Flask(__name__)
app.secret_key = os.environ.get('PICKY_KEY') #Your Flask app's secret key goes here

@app.route('/')
def index():
	return render_template('landing.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/browse', methods=['GET', 'POST'])
def process():

    location = flask_request.form['location_input'] #retrieve input from location box on landing page

    term = flask_request.form['searchterm_input'] #retrieve input from search term box on landing page

    businesses = execute(location, term) #Yelp query
    if businesses == None: #If Yelp query returns nothing
        flash('It seems like your location was invalid. Either try again later if you believe it should work or try a different location.')
        return redirect(url_for('index'))

    random.shuffle(businesses) #Prevent repetitive outcomes when using same search term

    business_name_list = []
    business_price_list = []
    business_url_list = []
    business_img_list = []
    business_distance_list = []
    business_rating_list = []
    counter = 0

    #Loop through each business found and append its images and Yelp URL to respective lists
    for business in businesses:
        info = business_info(businesses, counter)
        business_name_list.append(info[0])
        business_price_list.append(info[2])
        business_url_list.append(info[3])
        business_img_list.append(info[4])
        business_rating_list.append(info[5])
        business_distance_list.append(info[6])
        counter += 1

    #Provide the browse page with the images, Yelp URLS, and the number of businesses found
    return render_template('browse.html',
        name_list=business_name_list,
        price_list=business_price_list,
        url_list=business_url_list, 
        img_list=business_img_list, 
        rating_list=business_rating_list,
        distance_list=business_distance_list, 
        MAX_RESULTS=len(businesses))
if __name__ == '__main__':
	app.run()
