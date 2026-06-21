# SOC Secure Login System

## Overview
This project is a secure login application developed using Flask and bcrypt. It provides user registration, authentication, password hashing, and session management.

## Objective
To demonstrate secure authentication mechanisms and protect user credentials from unauthorized access.

## Features
- User Registration
- User Login Authentication
- Password Hashing using bcrypt
- Session Management
- Logout Functionality
- Secure Password Storage

## Technologies Used
- Python
- Flask
- bcrypt
- Session Management
- Web Application Security

## Project Structure
soc-secure-login-system/
│
├── secure_login_project.py
├── README.md
├── requirements.txt
└── screenshots/

## Installation

pip install flask bcrypt

## Run the Project

python secure_login_project.py

Application URL:
http://127.0.0.1:5000

## Application Endpoints

GET /
Displays application status.

POST /register
Registers a new user.

POST /login
Authenticates user credentials.

GET /logout
Logs out the authenticated user.

## Security Features
- Passwords are stored in hashed format.
- Plain-text passwords are not saved.
- Session management is used after successful authentication.
- Prevents unauthorized access to user accounts.

## SOC Use Case
SOC analysts and security engineers frequently assess authentication mechanisms and web application security. This project demonstrates secure password handling and user authentication practices used in modern web applications.
