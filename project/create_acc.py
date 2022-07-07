#!/usr/bin/python3
"""
Module is used to perform the operations
of creating an account
"""


import bcrypt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tables import User, Registration, Accounts

# contains string for the database
str1 = 'mysql://root:""@localhost:3306/WEKEZA'
# creates a connection to our database
engine = create_engine(str1)
DBSession = sessionmaker(bind=engine)
session = DBSession()

#stores all usernames that are existing
all_usernames = []

# Here we are storing all usernames in a list
for i in session.query(User.username).all():
    all_usernames.append(i[0])

# Here we take inputs from user and create an object
def create_account():
    username_1 = input("Enter UserName: ").strip()
    if username_1 in all_usernames:
        print("This username is already used choose another one")
        create_account()
    else:
        firstname_1 = input("Enter Your First Name: ")
        lastname_1 = input("Enter Your Last Name: ")
        password_1 = input("Enter Password: ")
        # hashedPassword = bcrypt.hashpw(password_1, bcrypt.gensalt())

        try:
            id_no_1 = int(input("Enter Your ID Number: "))
            PhoneNumber_1 = int(input("Enter Your Phone Number: "))
        except ValueError:
            print("Allowed Characters are Integers Only")
            create_account()
        else:
            user_1 = User(firstname = firstname_1, lastname=lastname_1,
                          id_no=id_no_1, PhoneNumber=PhoneNumber_1,
                          Password=password_1, username=username_1,
                          registration = [Registration(registrationfee=1000)],
                          account = [Accounts(acc_balance=0)])
            session.add(user_1)
            session.commit()
            print("You Have Successfully Created an Accout")
