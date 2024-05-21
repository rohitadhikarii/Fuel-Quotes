# Fuel-Quotes

# About the Project

This project was developed as part of a university course on software design. The goal of the project is to create a functional web application using Django, a high-level Python web framework. The application provides various features including user authentication, data management, and dynamic content rendering. Our team followed best practices in software development, including version control with Git, using virtual environments for dependency management, and writing unit tests to ensure code quality. This repository contains all the necessary files to set up and run the application locally, as well as detailed instructions on how to get started. We hope this project serves as a useful resource for understanding Django development and best practices in web application design.


## Prerequisites

Prerequisites

Before you begin, ensure you meet the following requirements:

Python (version 3 or higher recommended)

pip (Python package installer)

Virtualenv (optional but recommended for keeping dependencies isolated)

Installation

Follow these steps to get your development environment running:

1. Clone the repository

git clone https://github.com/Tavofn/Software_Design_Group_41.git

2. Install Django:

pip install django

Or

pip3 install django

2. Set up a virtual environment (Optional but recommended)

a. Create a virtual environment:

python -m venv venv

b. Activate the virtual environment:

On Windows:

venv\Scripts\activate

On Unix or MacOS:

source venv/bin/activate

3. Install requirements.txt

pip install -r requirements.txt

4. Navigate to the project directory

cd Group41

Running the Server

To run the Django development server:

python manage.py runserver

You should now be able to access your application at http://127.0.0.1:8000/.