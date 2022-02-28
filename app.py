from flask import Flask, render_template, redirect, url_for

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
    #return render_template("home.html", text="Dette er en hest!!!")
    return redirect(url_for('site2'))


@app.route('/site2')
def site():
    return render_template("site2.html")


""" ----------------------------------------------------------------
Start:
-----------------------------------------------------------------""" 
if __name__ == "__main__":
    app.run(debug=True)