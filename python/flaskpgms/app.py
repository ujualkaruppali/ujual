from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def index():
    return 'welcome to flask'
@app.route('/about')
def hij():
    return 'welcome to about'
@app.route('/home')
def hijk():
    return render_template('home.html')
@app.route('/icta')
def icta():
    return 'welcome to icta'

if(__name__=='__main__'):
    app.run(debug=True)

