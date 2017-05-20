from flask import session
from passlib.hash import sha256_crypt
from pymysql import escape_string
import gc

from helpers.db_connect import connect

SUCCESS = 'success'

def register(username, password, confirm):
    error = list()
    if len(username) == 0 or len(password)  == 0 or len(confirm) == 0:
        error.append('Please fill up the Registration form!')
        return error
    username = escape_string(username)
    password = sha256_crypt.encrypt(escape_string(password))
    confirm = escape_string(confirm)
    #accept_tos = request.form['accept_tos']
    conn, c = connect()
    if len(username) < 3 and len(confirm) < 3:
        error.append('Username and password must be above 3 characters')
    if not sha256_crypt.verify(confirm, password):
        error.append('Passwords do not match')
    query = c.execute("SELECT * FROM users WHERE username=(%s)", (username))
    if int(query) > 0:
        error.append('Username already exist')
    elif int(query) < 0:
        error.append('An error occured. Please try again')
####        if not accept_tos == 'on':
####            error.append('You need to accept the terms of service and privacy policy')
    if len(error) == 0:
        c.execute("INSERT INTO users VALUES('', %s, %s)",
                         (username, password))
        conn.commit()
        gc.collect()
        return SUCCESS
    gc.collect()
    return error


def login(username, password):
    error = list()
    if len(username) == 0 or len(password) == 0:
        error.append('Please fill up the login form')
        return error
    username = escape_string(username)
    password = sha256_crypt.encrypt(escape_string(password))
    conn, c = connect()
    query = c.execute("SELECT * FROM users WHERE username=(%s)",
                      (username))
    c.close()
    conn.close()
    if int(query) > 0:
        session['logged_in'] = True
        session['username'] = username
        gc.collect()
        return SUCCESS
    error.append('Invalid login credentials')
    return error
