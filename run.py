from flask import Flask,render_template
app = Flask(__name__)

# HOME PAGE
@app.route('/api/v1')
def index():
    return render_template('index.html')

# CONTACT PAGE
@app.route('/api/v1/contact')
def contact():
    return render_template('contact.html')


# About PAGE
@app.route('/api/v1/about')
def about():
    return render_template('about.html')

# DASHBOARD
@app.route('/api/v1/dashboard')
def dashboard():
    return 'Dashboard page'

# REGISTER
@app.route('/api/v1/adduser')
def addUsers():
    return render_template('register.html')

# LOGIN
@app.route('/api/v1/user')
def users():
    return render_template('login.html')

# CONFIGURATION
@app.route('/api/v1/config')
def config():
    return 'Configuraion page'

# MAKE ANALYSIS
@app.route('/api/v1/analysis')
def analysis():
    return 'add analysis page'

# VIEW ANALYSIS
@app.route('/api/v1/details')
def details():
    return 'view analysis page'

# VIEW PAST ANLYSIS
@app.route('/api/v1/history')
def history():
    return 'Analysis history page'

#VIEW ALL REGISTERED USERS
@app.route('/api/v1/report')
def report():
    return 'List of available users page'



if __name__ == '__main__':
    app.debug=True
    app.run(host = '0.0.0.0', port=5000)
