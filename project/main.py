#!/usr/bin/python3
"""
Defines main
"""

from create_acc import create_account
from login import login


welcome_message = "______________________________________________________________\n\t\tWEKEZA PROJECT\t\t\n\t\tWE MAKE TRANSACTIONS EASY\t\t\n\t\t$$\t\t$$\n\t\t$$\t\t$$\n\t\t$$\t\t\t$$\n\t\t\t$$\t\t$$\n\t\t\t$$\t$$\t"

def main():
    """
    This function contains the program flow, it 
    takes the user from one part of the system to aother
    """
    print(welcome_message)
    print("Press 1 to Create Account")
    print("Press 2 to Login")
    print("Press 3 to Exit")

    num = int(input())
    if num == 1:
        create_account()
        print()
        main()
    elif num == 2:
        login()
        print()
        main()
    elif num == 3:
        print("Byee")
        return
main()
