# Registration System

A simple web-based registration system built using Flask for the backend and Streamlit for the frontend. This application allows users to create, view, update, and delete registrations.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- Create new registrations with name, email, date of birth, phone number, and address.
- View all registrations.
- Update existing registrations by ID.
- Delete registrations by ID.

## Technologies Used

- **Backend**: Flask, SQLAlchemy, PostgreSQL
- **Frontend**: Streamlit
- **Database**: PostgreSQL

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/registration-system.git
   cd registration-system
2. **Install Required Packages: Make sure to install Flask, Flask-SQLAlchemy, Streamlit, and requests**:
   ```bash
   pip install Flask Flask-SQLAlchemy Streamlit requests psycopg2-binary
3. **Set Up PostgreSQL Database**:
   * Ensure PostgreSQL is installed and running.
   * Create a database named registration_db.
   * Update the connection string in your Flask app to match your PostgreSQL setup.
4. **Run the Flask Backend**:
   ```bash
   python your_flask_app.py
5. **Run the Streamlit Frontend: In a separate terminal, run**:
   ```bash
   streamlit run your_streamlit_app.py

## Usage
1. Open your web browser and navigate to http://localhost:8501 (can be different) to access the Streamlit frontend.
2. Use the "Create a New Registration" section to add a new registration.
3. Click "Load Registrations" to view all current registrations.
4. Use the "Update a Registration" section to modify existing entries.
5. Delete a registration by entering its ID in the "Delete a Registration" section.

## API Endpoints
### Create Registration
* POST /register
* Request Body:
  ```json
  {
    "Name": "Jack Johnson",
    "Email": "jacky123@example.com",
    "DateOfBirth": "1993-06-01",
    "PhoneNumber": "1234567890",
    "Address": "123 Main St"
  }
### Get All Registrations
* `GET /registrations`
### Get Registration by ID
* `GET /registrations/<id>`
### Update Registration by ID
* `PUT /registrations/<id>`
* Request Body:
  ```Json
  {
    "Name": "Jeane Smith",
    "Email": "jeanstar@example.com",
    "DateOfBirth": "1998-02-01",
    "PhoneNumber": "0987655671",
    "Address": "456 Main St"
  }
### Delete Registration by ID
* `DELETE /registrations/<id>`



