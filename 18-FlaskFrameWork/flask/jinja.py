from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def welcome():
    return "<html><h1>Welcome to the Flask Course</h1></html>"


@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


# Variable Rule
@app.route('/sucess/<int:score>')
def sucess(score):

    if score > 55:
        res = "PASSED"
    else:
        res = "FAILED"

    return render_template('result.html', result=res)


@app.route('/sucessres/<float:score>')
def sucessres(score):

    if score > 55:
        res = "PASSED"
    else:
        res = "FAILED"

    exp = {
        'score': score,
        'res': res
    }

    return render_template('result1.html', result=exp)


@app.route('/sucessif/<int:score>')
def sucessif(score):
    return render_template('result.html', result=score)


@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html', result=score)


@app.route('/submit', methods=['GET', 'POST'])
def submit():

    total_score = 0

    if request.method == 'POST':

        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])

        total_score = (science + maths + c + data_science) / 4

    return redirect(url_for('sucessres', score=total_score))


if __name__ == '__main__':
    app.run(debug=True)