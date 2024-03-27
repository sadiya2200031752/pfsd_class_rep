from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'
@app.route('/a')
def hello1():
    return 'Welcome to pfsd class'
@app.route('/emp/<int:emp1>')
def show(emp1) :
    return 'EMP ID number %d' %emp1
@app.route('/emp/<float:emp1>')
def show12(emp1) :
    return 'EMP ID number %f' %emp1
@app.route('/ex1')
def index():
    return render_template('hello.html')



if __name__ == "__main__":
    app.run(debug=True)