from flask_migrate import Migrate
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# 🔗 MySQL Database Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flaskuser:your_password@localhost/flaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# 🧾 Model Definition
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)

# 🏠 Home
@app.route('/')
def home():
    return "Flask API with MySQL is working!"

# ➕ Add user
@app.route('/api/user', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(name=data['name'], role=data['role'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User added", "id": new_user.id})

# 📋 Get users
@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name, "role": u.role} for u in users])

if __name__ == '__main__':
    app.run(debug=True)

