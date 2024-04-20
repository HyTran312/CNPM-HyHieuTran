from flask import render_template, request, redirect
from BanVeMayBay import app
import dao


@app.route("/")
def index():
    categories = dao.load_categories()
    return render_template('index.html', categories=categories)

@app.route('/login', methods=['get', 'post'])
def process_login_user():
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')

    return render_template('login.html')

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)
