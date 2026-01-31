from flask import Flask,render_template

app = Flask(__name__)  ##WSGI


@app.route("/")
def welcome():
    return "<html><h1>this is nikhil</h1></html>"
@app.route("/cart")
def cart():
    return render_template('cart.html')
@app.route("/about")
def about():
    return render_template('about.html')







if __name__=="__main__":
    app.run(debug=True)