#!/usr/bin/env python3
from flask import Flask
app = Flask(__name__)


#@app.route("/")
@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<parameter>')
def printing_string(parameter):
    print (parameter)
    return parameter

@app.route("/print/<string:parameter>")
def printed(parameter):
    print(f"{parameter}")
    return f"{parameter}"


#@app.route("/count/<int:parameter>")
@app.route('/count/<int:parameter>')
def counting(parameter):
    result = "\n".join(str(i) for i in range(parameter))
    # print(result)
    return result + "\n"

    result = '\n'.join(str(i) for i in range(parameter))
    return result + '\n'

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    result = None
    result = 0
    num1 = int(num1)
    num2 = int(num2)


    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation =="%":
        result = num1 % num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero"
    elif operation == '%':
        result = num1 % num2
        return 'Error: Zero Division error'
    else:
        return "Invalid operation"
        return "enter a valid input"

    return f'{result}'



    return str(result)


    if __name__ == "__main__":
        app.run(port=5555, debug=True)