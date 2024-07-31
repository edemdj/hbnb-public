from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__, template_folder='base_files', static_folder='base_files')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    # Simuler la vérification des identifiants
    if email == 'john@example.com' and password == 'password123':
        return jsonify({"access_token": "fake-jwt-token"}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

@app.route('/place')
def place_page():
    return render_template('place.html')

@app.route('/add_review')
def add_review_page():
    return render_template('add_review.html')

if __name__ == '__main__':
    app.run(port=8000)
