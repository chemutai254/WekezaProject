#!/usr/bin/python3
"""
Module is used to perform the operations
of creating an account
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from users import User

# contains string for the database
str1 = 'mysql://root:""@localhost:3306/WEKEZA'
# creates a connection to our database
engine = create_engine(str1)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Here we take inputs from user and create an object
user_1 = User(username = input("Enter UserName: "),
              firstname = input("Enter Your First Name: "),
              lastname = input("Enter Your Last Name: "),
              id_no = int(input("Enter Your ID Number: ")),
              PhoneNumber = int(input("Enter Your Phone Number: ")),
              Password = input("Enter Your Password: "))
session.add(user_1)
session.commit()
