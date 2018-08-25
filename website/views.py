import os, random, string
from flask import render_template, request, flash, redirect, url_for
from website import hyperlinks


@hyperlinks.context_processor
def inject_data():
    """
    This method is used to load global variables
    to the base templates of the application.
    Feel free to get values from your database
    """
    base= {'author': 'Kenvin Emiewo', 'language' : 'python 3', 'framework' : 'Flask'}
    return dict(base_data= base)


@hyperlinks.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@hyperlinks.route("/")
def index():
    """
    This function creates the index page
    :return: a template index.html
    """
    return render_template("index.html")



@hyperlinks.route("/contact-us")
def contact_us():
    """
    This function creates the contact us page
    :return: a template contact.html
    """
    return render_template("contact.html")
