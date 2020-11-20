from flask import Flask, redirect, render_template, request, session, url_for


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
