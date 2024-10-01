from flask import *

app = Flask(__name__)

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/')
@app.route('/login.html')
def login():
   return render_template('login.html')

@app.route('/register.html')
def register():
   return render_template('register.html')

@app.route('/forgot-password.html')
def forgot_password():
   return render_template('forgot-password.html')

@app.route('/404.html')
def not_found():
   return render_template('404.html')

if __name__ == '__main__':
  app.run(debug=True)
