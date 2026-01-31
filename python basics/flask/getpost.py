from flask import Flask,render_template,request

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
@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=='POST':
        name=request.form.get('name')
        return f'hello {name}!'
    return render_template('login.html')


@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form.get('name')
        return f'hello {name}!'
    return render_template('login.html')
    
    
        







if __name__=="__main__":
    app.run(debug=True)