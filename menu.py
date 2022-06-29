#!/usr/bin/python3
"""
Defines a function menu
"""


def menu(arg):
    """
    Used to Display a menu to the customer for her
    to manouver around the application

    arg(int): Integer used to determine flow of work
    """
    match arg:
        case 1:
            print("You Have Entered Withdrawal Section")
            return
        case 2:
            print("You have Entered Deposits Section")
            return
        case 3:
            print("You have Entered Check Balances Section")
            return
        case 4:
            print("You have Entered Check Withdrawal History")
            return
        case 5:
            print("You have Entered Check Deposit History")
            return
        case 6:
            print("You have Entered Exit")
            return
