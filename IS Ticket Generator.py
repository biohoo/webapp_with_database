#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 19:09:15 2018

@author: jonathanrice

From Jeff Knupp Youtube: Writing Idiomatic Python

Identify the:
    
    Nouns (objects)
    Verbs (methods)
    Adjectives (class parameters)
    Adverbs (method parameters)
    
Create, Read, Update, Delete (CRUD)
(Like IS tickets)

a function should do one and only one logical thing.

used sqlite3 to create table and placed
in Desktop/Pyth

CREATE TABLE ticket (
id INT PRIMARY KEY,
change TEXT NOT NULL,
title TEXT NOT NULL,
description TEXT,
submitter_name TEXT,
submitter_email TEXT,
submitter_website TEXT,
file TEXT,
date_created DATE NOT NULL
)

In a REST API you have resources (nouns) in a system
collections (group of resources)
to display collection


"""
from flask import Flask, render_template  #flask works as an application object
import sqlite3


app = Flask(__name__)


@app.route('/', methods=['GET']) # lives at directory root. GET method allowed.
def list_tickets():
    '''display a list of tickets in the system.'''

    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()    # Keeps track of transaction
    cursor.execute('SELECT * FROM ticket')
    all_tickets = cursor.fetchall()
    
    #   Flask expects a folder "templates" to be created for this to exist.
    
    return render_template('index.html', tickets=all_tickets)
    

@app.route('/ticket', methods=['GET','POST'])   #GET ticket before POSTing 
def enter_ticket():
    '''Enter a new ticket via a form.'''

    return render_template('edit.html')
    #return '<b>enter_ticket</b>'

@app.route('/ticket/<int:ticket_id>')    #   Variables supported bracket
def view_ticket(ticket_id):
    '''display the details of ticket with ID *ticket_id*'''

    return 'view_ticket {}'.format(ticket_id)

if __name__ == '__main__':
    app.run(debug=True)
