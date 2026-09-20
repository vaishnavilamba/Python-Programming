from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def welcome():
    return "<h1>Welcome to the Flask Course</h1>"


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/submit', methods=['POST'])
def submit():

    science = float(request.form['science'])
    maths = float(request.form['maths'])
    c = float(request.form['c'])
    data_science = float(request.form['datascience'])

    total_score = (science + maths + c + data_science) / 4

    print("Science:", science)
    print("Maths:", maths)
    print("C:", c)
    print("Data Science:", data_science)
    print("Total Score:", total_score)

    return redirect(url_for('sucessres', score=total_score))


@app.route('/sucessres/<float:score>')
def sucessres(score):

    if score > 55:
        res = "PASSED"
    else:
        res = "FAILED"

    result = {
        'score': score,
        'result': res
    }
    
    return render_template('result1.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)