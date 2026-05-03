# utils.py

# Code Smell: too many parameters
def create_profile(name, age, email, phone, address, city, country):
    print(name, age, email, phone, address, city, country)

# Duplicate code
def greet_user(user):
    if user is None:
        return "Hello Guest"
    return "Hello " + user

def greet_admin(admin):
    if admin is None:       # same logic repeated
        return "Hello Guest"
    return "Hello " + admin