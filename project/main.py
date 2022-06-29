#!/usr/bin/python3
"""
Defines main
"""

from create_acc import create_account
from login import login


welcome_message = "______________________________________________________________\n\t\tWEKEZA PROJECT\t\t\n\t\tWE MAKE TRANSACTIONS EASY\t\t\n\t\t$$\t\t$$\n\t\t$$\t\t$$\n\t\t$$\t\t\t$$\n\t\t\t$$\t\t$$\n\t\t\t$$\t$$\t"

def main():
    print("Press 1 to Create Account")
    print("Press 2 to Login")

    num = int(input())
    if num == 1:
        create_account()
        main()
    elif num == 2:
        login()
        main()
main()
