from flask import Flask,render_template ,request

from data import Students

app=Flask(__name__)

getStudents=Students()

@app.route('/students')
def stud():
    return render_template('studentlist.html',mystudentsList=getStudents)


@app.route('/send',methods=['GET','POST'])
def send():
    if(request.method=='POST'):
        getName=request.form['nm']
        return render_template('result.html',newName=getName)
def index():
    return render_template('home.html') 
@app.route('/about')
def abt():
    return render_template('about.html')

@app.route('/home')
def hme():
    return render_template('home.html')

@app.route('/contact')
def cnt():
    return render_template('contact.html')


if(__name__=='__main__'):
    app.run(debug=True)

