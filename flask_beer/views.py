# import and setup modules we'll be using in this notebook

import flask

from flask import render_template
from flask import request

from flask_beer import app
#from forms import InputForm
from flask_beer.models.input_form_model import InputForm
from flask_beer.models import beer_model_2
import logging
import os
import re
import pandas as pd

beer = pd.read_csv('~/Dropbox/beer_scrape/cleaned_data/all_beers.csv')
beer_with_desc = beer[beer.description.str.contains('No notes at this time.') == False]
beer_with_desc.reset_index()
documents = beer_with_desc['description'].tolist()

@app.route('/', methods=["GET", "POST"])

@app.route('/index', methods=["GET", "POST"])

def index():
    form = InputForm(request.form)

    if request.method == 'POST' and form.validate():
        result = beer_model_2.get_beers(form.good.data, form.bad.data)
        print(result)

        return flask.render_template('output_beer.html', 
                                     beer_list=result)
        
    else:
        result = None
        
        return flask.render_template('homepage_2.html',
                                     form=form)


if __name__ == '__main__':
    app.run(debug=True)

@app.route('/index_val', methods=["GET", "POST"])

def index_val():
    form = InputForm(request.form)

    if request.method == 'POST' and form.validate():
        result = beer_model_2.get_beers(form.good.data, form.bad.data)
        print(result)

        return flask.render_template('output_beer.html', 
                                     beer_list=result)
        
    else:
        result = None
        
        return flask.render_template('homepage_2.html',
                                     form=form)


if __name__ == '__main__':
    app.run(debug=True)
    

    
@app.route('/about')
def about_bt():
    return flask.render_template('about_bt.html')

    
    
@app.route('/input', methods=["GET", "POST"])
def beer_input():
    form = InputForm(request.form)

    if request.method == 'POST' and form.validate():
        result = beer_model_2.get_beers(form.good.data, form.bad.data)
        
    #else:
        #result = None
        
        return flask.render_template('homepage_3.html',
                                     form=form, result = result)


@app.route('/output')
def beer_output():
    result = request.args.get.result
    return flask.render_template('output_beer.html', 
                                     beer_list=result)