from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/math', methods=['POST'])
def math_ops():
    calculate = 0 
    if (request.method == 'POST'):
        ops = request.form['operation']
        num_1 = int(request.form['num_one'])
        num_2 = int(request.form['num_two'])
        if (ops == 'add'):
            calculate = num_1 + num_2
        elif (ops == 'sub'):
            calculate = num_1 - num_2
        elif (ops == 'divide'):
            calculate = num_1 / num_2
        elif (ops == 'multiply'):
            calculate = num_1 * num_2
    return render_template('result.html',result = calculate)


# to check api in postman

@app.route('/postman', methods=['POST'])
def math_ops1():
    calculate = 0
    if (request.method == 'POST'):
        ops = request.json['operation']
        num_1 = int(request.json['num_one'])
        num_2 = int(request.json['num_two'])
        if (ops == 'add'):
            calculate = num_1 + num_2
        elif (ops == 'sub'):
            calculate = num_1 - num_2
        elif (ops == 'divide'):
            calculate = num_1 / num_2
        elif (ops == 'multiply'):
            calculate = num_1 * num_2

    return jsonify(calculate)


if __name__ == '__main__':
    app.run(host='0.0.0.0')