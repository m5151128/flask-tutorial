import functools

from flask import Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)
app.config.from_object('config')
app.secret_key = 'hogehoge'

db = SQLAlchemy(app)

toolbar = DebugToolbarExtension(app)
