from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # If you plan to allow cross-origin requests

app = Flask(__name)
CORS(app)  # Enable CORS if you plan to allow cross-origin requests (e.g., for frontend hosted on a different domain)

# Set up your PostgreSQL database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://your_database_connection_string'
db = SQLAlchemy(app)

# Define the User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Check if the username is already in use
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'message': 'Username is already taken'}), 400

    # Create a new user and save it to the database
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Registration successful'})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
