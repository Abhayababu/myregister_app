from flask import Flask, redirect, request, url_for, render_template

app = Flask(__name__)
app.secret_key = "your_secret_key"
users = {}

@app.route("/")
def home():
    return redirect(url_for('login'))

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pass
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)
