from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)  ##WSGI


@app.route("/")
def welcome():
    return "<html><h1>this is nikhil</h1></html>"
@app.route("/cart",methods=['GET'])
def cart():
    return render_template('cart.html')
@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form.get('name')
        return f'hello {name}!'
    return render_template('login.html')
##variable rule
# @app.route('/success/<int:score>')
# def success(score):
#     res="" 
#     if score>=50:
#         res="PASS"
#     else:
#         res="FAIL"
    
#     return render_template('result.html',results=res)

@app.route('/successres/<float:score>')
def successres(score):
    res="" 
    if score>=50:
        res="PASS"
    else:
        res="FAIL"

    exp={'score':score,'res':res}
    
    
    
    return render_template('result.html',results=exp)

@app.route('/submit1',methods=['GET','POST'])
def submit1():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        datascience=float(request.form['datascience'])

        total_score=(science+maths+c+datascience)/4
    else:
        return render_template('getresults.html')
    
    return redirect(url_for('successres',score=total_score))

if __name__=="__main__":
    app.run(debug=True)