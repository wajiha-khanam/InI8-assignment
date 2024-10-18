from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

# Database configuration (PostgreSQL)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/registration_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# The Registration model
class Registration(db.Model):
    __tablename__ = 'Registration'

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(100), nullable=False)
    Email = db.Column(db.String(255), unique=True, nullable=False)
    DateOfBirth = db.Column(db.String(10), nullable=False)
    PhoneNumber = db.Column(db.String(15), nullable=True)
    Address = db.Column(db.String(255), nullable=True)
    RegistrationDate = db.Column(db.DateTime, server_default=db.func.now())

# Initializing the database
with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def create_registration():
    try:
        data = request.get_json()
        new_registration = Registration(
            Name=data['Name'],
            Email=data['Email'],
            DateOfBirth=data['DateOfBirth'],
            PhoneNumber=data.get('PhoneNumber'),
            Address=data.get('Address')
        )
        db.session.add(new_registration)
        db.session.commit()
        return jsonify({"message": "Registration created successfully!"}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Email already exists!"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/registrations', methods=['GET'])
def get_registrations():
    registrations = Registration.query.all()
    output = []
    for reg in registrations:
        registration_data = {
            'ID': reg.ID,
            'Name': reg.Name,
            'Email': reg.Email,
            'DateOfBirth': reg.DateOfBirth,
            'PhoneNumber': reg.PhoneNumber,
            'Address': reg.Address,
            'RegistrationDate': reg.RegistrationDate
        }
        output.append(registration_data)
    return jsonify(output), 200

@app.route('/registrations/<int:id>', methods=['GET'])
def get_registration(id):
    registration = Registration.query.get_or_404(id)
    return jsonify({
        'ID': registration.ID,
        'Name': registration.Name,
        'Email': registration.Email,
        'DateOfBirth': registration.DateOfBirth,
        'PhoneNumber': registration.PhoneNumber,
        'Address': registration.Address,
        'RegistrationDate': registration.RegistrationDate
    }), 200

@app.route('/registrations/<int:id>', methods=['PUT'])
def update_registration(id):
    data = request.get_json()
    registration = Registration.query.get_or_404(id)
    try:
        registration.Name = data['Name']
        registration.Email = data['Email']
        registration.DateOfBirth = data['DateOfBirth']
        registration.PhoneNumber = data.get('PhoneNumber', registration.PhoneNumber)
        registration.Address = data.get('Address', registration.Address)
        db.session.commit()
        return jsonify({"message": "Registration updated successfully!"}), 200
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Email already exists!"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/registrations/<int:id>', methods=['DELETE'])
def delete_registration(id):
    registration = Registration.query.get_or_404(id)
    try:
        db.session.delete(registration)
        db.session.commit()
        return jsonify({"message": "Registration deleted successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
