from flask import Flask, request, render_template, redirect, url_for
from flask.json import jsonify

app = Flask(__name__)

@app.route("/", methods=['GET'])
def main():
    return "<h1>main</h1>"

@app.route("/index", methods=['GET'])
def index():
    return "<center><h1>index</h1></center>"

@app.route("/square/<int:num>")
def square(num):
    return str(num**2)

@app.route("/cube/<int:num>")
def cube(num):
    return str(num**3)

@app.route("/form", methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template("form.html")
    else:
        p = float(request.form['P'])
        c = float(request.form['C'])
        m = float(request.form['M'])
        avg = (p+c+m)/3
        if avg>=50:
            res = "square"
        else:
            res = "cube"

        return redirect(url_for(res, num=avg))

        # return render_template('form.html', score=avg)
    
@app.route('/api', methods=['POST'])
def sm():
    data = request.get_json()
    x = float(dict(data)['a'])
    y = float(dict(data)['b'])
    return jsonify(x+y)

if __name__ == "__main__":
    app.run(debug=True)