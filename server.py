import os
from scripts.check import Check 
from flask import Flask, request, render_template

app = Flask(__name__, static_folder='public', template_folder='views')
app.secret_key = os.environ.get('SECRET')

@app.route('/')
def index():
    return render_template('loginPage.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if Check.login(username, password):
        return render_template('index.html')
    else:
        return render_template('loginPage.html')
    
@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/loginPage')
def loginPage():
    return render_template('loginPage.html')

@app.route('/submit_registration', methods=['POST'])
def submit_registration():
    try:
        username  = request.form.get('rname'    )
        surname   = request.form.get('rsurname' )
        email     = request.form.get('remail'   )
        phone     = request.form.get('rphone'   )
        password  = request.form.get('rpassword')
        Check.signup(email, username, surname, phone, password)
        return render_template('index.html')
    except :
        return render_template('register.html', error="Request error occurred.")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
