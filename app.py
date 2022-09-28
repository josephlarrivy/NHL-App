from flask import Flask, render_template
app = Flask(__name__)
if __name__ == '__main__':
    app.run

@app.route('/')
def homepage():
    """return homepage"""
    return render_template('home.html')