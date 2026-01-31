from flask import Flask

app = Flask(__name__)  ##WSGI


@app.route("/")
def welcome():
    return "Hello world"
@app.route("/cart")
def cart():
    return "Welcome to cart page"







if __name__=="__main__":
    app.run(debug=True)