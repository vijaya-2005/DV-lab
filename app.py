from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash

app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = "your_secret_key_here"  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        full_name = request.form['full_name']
        username = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        gender = request.form.get('gender')

        # Check if passwords match
        if password != confirm_password:
            flash("Passwords do not match. Please try again.", "danger")
            return redirect(url_for('index'))

        # Hash the password
        hashed_password = generate_password_hash(password)

        # Debugging print (Replace with database storage)
        print(f"Full Name: {full_name}, Username: {username}, Email: {email}, Phone: {phone}, Hashed Password: {hashed_password}, Gender: {gender}")

        flash("Registration successful!", "success")  
        return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('success.html')  # Displays success message properly

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
