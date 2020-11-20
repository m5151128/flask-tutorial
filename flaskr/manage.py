from app import *
from app.models.post import Post
from app.models.user import User
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from werkzeug.security import check_password_hash, generate_password_hash


migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


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
