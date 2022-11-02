from my_ldap import *
from flask import Flask, render_template, request, flash, redirect, url_for, session


app = Flask(__name__)
app.secret_key = 'super secret key'


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        full_name = request.form.get("full_name")
        password = request.form.get("password")
        session['user'] = full_name
        login_success = connect_ldap_server(full_name, password)
        if login_success:
            return redirect(url_for('google_auth'))
        else:
            error = 'Invalid credentials'
    return render_template('login.html', error=error)


@app.route("/google_auth", methods=["GET", "POST"])
def google_auth():
    if request.method == "POST":
        if request.form['submit_button'] == 'Request QR code':
            user = session['user']
            qr_url = create_qr_code(user)
            return render_template('google_auth.html', qr_url1=qr_url)
        elif request.form['submit_button'] == 'send':
            google_code = request.form.get("google_authenticator")
            verified = check_google_code(google_code)
            if verified:
                flash("Login success")
                return render_template('google_auth.html')
            else:
                flash("Login failed")
                return render_template('google_auth.html')
    else:
        return render_template("google_auth.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0")




