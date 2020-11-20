import functools

from flask import Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config.from_object('flaskr.config')
app.secret_key = 'hogehoge'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

toolbar = DebugToolbarExtension(app)


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('login'))

        return view(**kwargs)

    return wrapped_view


@app.before_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.filter_by(id=user_id).first()


if __name__ == '__main__':
    app.run(debug=True)
    # app.register_blueprint(auth.bp)

    manager.run()
