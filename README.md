CRUD Application with Flask and MySQL
Overview
This is a basic CRUD (Create, Read, Update, Delete) application using Flask and MySQL. It demonstrates how to perform these operations on a sample dataset stored in a MySQL database.

Requirements
Python 3.x
Flask
MySQL
MySQL Connector for Python
Installation
Clone the Repository

bash
Copy code
git clone https://github.com/username/repository-name.git
cd repository-name
Set Up a Virtual Environment

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies

bash
Copy code
pip install -r requirements.txt
Configure the Database

Update the config.py file with your MySQL credentials.

Create the Database and Table

Run the provided SQL script to set up the database and table.

Usage
Run the Application

bash
Copy code
python app.py
Access the Application

Open your browser and go to http://127.0.0.1:5000.

Endpoints
GET /records: View all records.
POST /records: Add a new record.
GET /records/<id>: View a specific record.
PUT /records/<id>: Update a specific record.
DELETE /records/<id>: Delete a specific record.
