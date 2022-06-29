#!/usr/bin/python3
"""
Defines a function menu
"""

from deposit import deposit
from withdraw import withdraw
from transactions import transactions

def prompt_message():
    print("Press 1 To Withdraw\tPress 2 To Deposit")
    print("Press 3 To Check Balance\tPress 4 To Check Deposit History")
    print("Press 5 To Withdrawal History")

def menu(user_details):
    """
    Used to Display a menu to the customer for her
    to manouver around the application

    arg(int): Integer used to determine flow of work
    """
    prompt_message()
    arg = int(input())
    if arg == 1:
        print("You Have Entered Withdrawal Section")
        withdraw(user_details)
        return
    if arg == 2:
        print("You have Entered Deposits Section")
        deposit(user_details)
    elif arg == 3:
        transactions(arg, user_details)
        return
    elif arg == 4:
        transactions(arg, user_details)
        return
    elif arg == 5:
        transactions(arg, user_details)
        return
    elif arg == 6:
        transactions(arg, user_details)
        return
