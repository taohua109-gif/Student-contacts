# Contacts Backend API

A Flask-based RESTful API for managing contacts.

## Features
- CRUD operations for contacts
- Contact grouping
- Search functionality
- CORS enabled for frontend integration

## Installation
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python run.py`

## API Endpoints
- `GET /api/contacts` - Get all contacts
- `POST /api/contacts` - Create new contact
- `PUT /api/contacts/:id` - Update contact
- `DELETE /api/contacts/:id` - Delete contact
- `GET /api/contacts/search?q=:query` - Search contacts

## Running the Application
 bash
 # Navigate to the project directory
 # Make sure you are in the project root directory
 cd "Student ID_contacts_backend"
pip3 install -r requirement.txt
python3 run.py