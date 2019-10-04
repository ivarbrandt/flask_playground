from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def playground():
    return render_template("playground.html", num = 4)

@app.route('/play/<x>')
def playground1(x):
    return render_template("playground.html", num = int(x))

@app.route('/play/<x>/<color>')
def playground2(x, color):
    return render_template("playground.html", num = int(x), color = color )


if __name__=="__main__":
    app.run(debug = True)