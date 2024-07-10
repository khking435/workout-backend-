from flask import Flask

app = Flask(__name__)

@app.route('/')
def Fit_fussion():
    return 'Hello, Fitness a bWorld!'

if __name__ == '__main__':
    app.run(debug=True)
