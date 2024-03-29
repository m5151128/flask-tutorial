import functools

from application import app, db
from app.models import Post, User
from datetime import datetime
from flask import flash, g, redirect, render_template, request, session, url_for
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from werkzeug.security import check_password_hash, generate_password_hash

migrate = Migrate(app, db)
toolbar = DebugToolbarExtension(app)


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('login'))

        return view(**kwargs)

    return wrapped_view


@app.route('/')
def index():
    posts = Post.query.join(Post.users).order_by(Post.created_at).all()
    users = User.query.all()
    return render_template('blog/index.html', posts=posts, users=users)


@app.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            new_post = Post(title=title, body=body, user_id=session.get('user_id'))
            db.session.add(new_post)
            db.session.commit()

            return redirect(url_for('index'))

    return render_template('blog/create.html')


@app.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    # post = get_post(id)
    post = Post.query.get_or_404(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            post.title = title
            post.body = body
            post.updated_at = datetime.now()
            db.session.commit()

            return redirect(url_for('index'))

    return render_template('blog/update.html', post=post)


@app.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    # get_post(id)
    post = Post.query.get_or_404(id)

    db.session.delete(post)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        user = User.query.filter_by(name=username).first()

        if user is None:
            new_user = User(name=username, password=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('login'))

        error = 'User {} is already registered.'.format(username)

        flash(error)

    return render_template('auth/register.html')


@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        user = User.query.filter_by(name=username).first()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user.password, password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')


def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post


@app.before_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.filter_by(id=user_id).first()


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


# if __name__ == '__main__':
    # manager.run()
