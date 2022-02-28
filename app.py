from flask import Flask, render_template, redirect, url_for
import json

""" ----------------------------------------------------------------
App Configuration:
-----------------------------------------------------------------""" 
app = Flask(__name__)
app.config['SECRET_KEY'] = "MySecretHashValue"



""" ----------------------------------------------------------------
Routes:
-----------------------------------------------------------------""" 
@app.route('/')
def home():
    return redirect(url_for('site2'))


@app.route('/site2')
def site2():
    data = [
        {
        "id":1
        ,"name":"name 1"
    }
    ,{
        "id":2
        ,"name":"name 2"
    }
    ,{
        "id":3
        ,"name":"name 3"
    }
    ]
    return render_template("site2.html", data=data)

""" ----------------------------------------------------------------
Start:
-----------------------------------------------------------------""" 
if __name__ == "__main__":
    app.run(debug=True)