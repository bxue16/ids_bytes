"""`main` is the top level module for your Flask application."""
# Imports
import os
import jinja2
import webapp2
import logging

# [START app]
import logging

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)



# [START imports]
from flask import Flask, render_template, request
    
# Import the Flask Framework
app = Flask(__name__)

@app.route('/')
def hello():
    template = JINJA_ENVIRONMENT.get_template('templates/index.html')
    return template.render()
 
