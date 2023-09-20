from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  # Print the string to the console.
    return parameter  # Display the string in the browser.

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = "<br>".join([str(i) for i in range(1, parameter + 1)])
    return numbers

@app.route('/math/<int:num1>+<int:num2>')
def add(num1, num2):
    return str(num1 + num2)

@app.route('/math/<int:num1>-<int:num2>')
def subtract(num1, num2):
    return str(num1 - num2)

@app.route('/math/<int:num1>*<int:num2>')
def multiply(num1, num2):
    return str(num1 * num2)

@app.route('/math/<int:num1>div<int:num2>')
def divide(num1, num2):
    if num2 == 0:
        return "Division by zero error!"
    return str(num1 / num2)

@app.route('/math/<int:num1>%<int:num2>')
def modulus(num1, num2):
    return str(num1 % num2)

if __name__ == '__main__':
    app.run(port=5555)
