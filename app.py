# app.py

import os

# Bug: division by zero possible
def divide(a, b):
    return a / b

# Vulnerability: hardcoded password
password = "admin123"

# Code Smell: unused variable
x = 10

# Bug: function with no return check
def get_name(user):
    return user["name"]   # crash if user is None