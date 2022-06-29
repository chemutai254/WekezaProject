#!/usr/bin/python3
"""
Defines a function login
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tables import User
from menu import menu

# contains string for the database
str1 = 'mysql://root:""@localhost:3306/WEKEZA'
# creates a connection to our database
engine = create_engine(str1)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    results = session.query(User).filter(User.username == username).first()
    if results is None:
        print("User Does Not Exist Kindly Create an Account")
    elif password == results.Password:
        print("SuccessFull Login")
        menu(results)
    else:
        print("Wrong Password")
        login()
