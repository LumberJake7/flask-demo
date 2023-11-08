from flask import Flask, request, jsonify

app = Flask(__name__)


operations = {
    "add": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mult": lambda a, b: a * b,
    "div": lambda a, b: a / b if b != 0 else "Division by zero is not allowed",
}

@app.route('/math/<operation>')
def math(operation):
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))

    if operation in operations:
        result = operations[operation](a, b)
        return jsonify({'result': result})
    else:
        return "Invalid operation", 400

if __name__ == '__main__':
    app.run(debug=True)
    
# @app.route('/add')
# def add():
#     a = float(request.args.get('a', 0))
#     b = float(request.args.get('b', 0))
#     result = a + b
#     return jsonify({'result': result})

# @app.route('/sub')
# def subtract():
#     a = float(request.args.get('a', 0))
#     b = float(request.args.get('b', 0))
#     result = a - b
#     return jsonify({'result': result})

# @app.route('/mult')
# def multiply():
#     a = float(request.args.get('a', 0))
#     b = float(request.args.get('b', 0))
#     result = a * b
#     return jsonify({'result': result})

# @app.route('/div')
# def divide():
#     a = float(request.args.get('a', 0))
#     b = float(request.args.get('b', 1)) 
#     result = a / b
#     return jsonify({'result': result})

# if __name__ == '__main__':
#     app.run(debug=True)
