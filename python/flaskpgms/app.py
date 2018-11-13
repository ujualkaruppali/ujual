



from flask import Flask,render_template ,request
app=Flask(__name__)

@app.route('/send',methods=['GET','POST'])
def send():
    if(request.method=='POST'):
        getName=request.form['nm']
        return render_template('result.html',newName=getName)
       

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

