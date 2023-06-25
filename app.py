from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/cards')
def cards():
    return render_template("cards.html")


@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    if request.method == 'POST':
        form_data = request.form
    return render_template("signup.html")

@app.route('/', methods=['GET', 'POST'])
def form_submission():
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        emailaddress = request.form.get('emailaddress')
        number = request.form.get('number')
        dob = request.form.get('dob')
        location = request.form.get('location')
        skill = request.form.get('skill')
        domain = request.form.get('domain')
        exp = request.form.get('exp')
        qua = request.form.get('qua')

        return 'Form submitted successfully!'
    # Display the form
    return render_template('home.html')


if __name__ == '__main__':
    app.run()
