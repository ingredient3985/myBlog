from flask import request,redirect,url_for,render_template,flash,session
from myBlog import app


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            flash("ユーザー名が違います")
        elif request.form['password'] != app.config['PASSWORD']:
            flash('パスワードが違います')
        else:
            session['logged_in'] = True
            flash('ログインしました')
            return redirect('/')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('ログアウトしました')
    return redirect(url_for('show_entries'))

@app.errorhandler(404)
def non_existant_route(error):
    return redirect(url_for('login'))