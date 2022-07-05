# WEKEZA PROJECT 

- WEKEZA is a project meant to assist small financial groups automate their transaction processes such as deposits, withdrawals, and loan processing targeting small financial groups such as "CHAMA" in Kenya.
- WEKEZA simply provides solutions such as:
	1. Storage of the user data in a database
	2. Automated transactions
---

# PROCESSES
## Creation of an Account
- The system allows creation of an account to new users and ensures each of the users are eligible to the requirementsof the roup such as registration fees and age.
- When a user creates an account he or she is prompted to fill all the fields which upon completion is stored in the database.

  ![Alt text](/img/create_acc.png)
---

## Logging into the System
- The system validates logging into the system. Fisrt, the user is prompted to enter the username. During account creation, the system ensures that a unique username is created.
- The system then prompts the user to enter their password where the entered password is subjected to validation. The system counterchecks the existing password and the entered password for validation. If the account exists, the user is sucessfully logs into the system where they view the menu.
- On the contrary, if there is a mismatch between the created and entered credentials, the system displays the appropriate error message where they are taken back to the login page.

  ![Alt text](/img/login.png)
---

# Components of a Menu
- The system consists of modules such as:
	1. Deposits
	2. Withrawals
	3. Checking account balances
	4. Checking deposit history
	5. Checking withdrawal history
- The system prompts the user upon validation to enter the specified option in which to transact.

  ![Alt text](/img/menu.png)
---

### Deposits
- The system prompts the user to enter the amount of money to deposit into the account. The system verifies whether the inputted amount meets the group requirement or not. If it does not, the appropriate message is displayed to the user.
- If the amount meets the system requirements, the amount is deposited with the transaction registered into the database and the user displayed with the success message.

  ![Alt text](/img/deposits.png)
---

### Withdrawals
- The system prompts the user to enter the withdrawal amount where it undergoes some system validation to ensure the amount inputted meets the group requirement. If the amount is greater than the account balance, an appropriate error message is displayed to the user.
- But upon successful validation, the system records the transaction details and update the balance of the customer. Additionally, the success message will be displayed to the user on complete transaction.

  ![ALt text](/img/withdrawals.png)
---

### Other Processes
- The system returns the outputs of account balance, withdrawals and deposits upon queried by the user.

   ![Alt text](/img/balance.png "Account balance")


   ![Alt text](/img/with_hist.png "Withdrawal history")


   ![Alt text](/img/dep_his.png "Deposits history")
---

## Features yet to be Implemented
1. Loan Processing
2. Monthly and Weekly contributions.
---
