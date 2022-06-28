wekeza 
==============================


# AUTHOURS 
 * Nancy chemutai
 * Rodyne 
 * Brian kiplangat


###########

* Initial account balance can be set on startup
* Interactive user input
* Deposit into account
* Withdraw from account
* List all transactions

A simple transaction list might look like this:

```
      op       amount     balance
   --------  ----------  ----------
                              50.00  (starting)
   deposit        15.00       65.00
   deposit       125.01      190.01
   withdraw       25.00      165.01
```


Requirements
------------

* Python 3
* A text editor or IDE (Integrated Development Environment)
* A shell to execute your scripts from
  
The Community Edition is free.
It has a built in shell and debugger for running your scripts, as well as many other features. 




#### 
 show account balance.

* integer and string literals
* variable
* assignment operator
* format operator
* format integer field
* expression

####  

Show a $10 withdrawal and a $20 deposit.

* print empty line
* function call with no arguments
* compound assignment operators

#### 

Show a $30 withdrawal and a $15 deposit.

* the tedium of repetition

#### 

Factor both withdrawals and factor both deposits.

* function definition
* function calling
* code factoring
* global variables
* indentation

#### 

Factor show balance.

* more factoring
* function definition with no arguments

#### 

Reorder code to group functions.

* code reorg: functions first

#### 

Create function for main code.

* code reorg: more function grouping

#### 

Allow user to supply transaction amounts.

* user input
* string conversion to integer

#### 

Have only 1 transaction, but allow user to determine which type.

* string input and equality comparison
* conditional statement with else clause (branching)

#### 

Allow unlimited transactions.

* looping
* break out of a loop
* Boolean literal
* single-branch conditional statement

#### 

Add error checking for each prompt.

* error checking
* syntax errors
* exception handling
* continue statement to skip rest of loop
* inequality comparison
* "and" logical operator

#### 

Add semantic error checking for transaction.

* semantic errors
* ordering comparison
* single-quotes vs double-quotes

#### 

Flatten the logic in main().

* code reorg: reduce nesting

#### 

Refactor again and simplify main().

* None object
* is operator
* pass statement
* else-if clause of conditional statement
* "not" logical operator

#### 
Fix bug.

* the importance of initializing reused variables sometimes
* why testing is important

#### 

Rename 'type' to 'op' for operator.

* the importance of naming
* identifiers sometimes need to change as code evolves

#### 
List Operations

Summary of basic list operations.  *This lesson was hacked in after the tutorial was
completed to address the big jump to lists and lists of lists in Lesson 17.*

* create a list of simple elements
* display a list
* create an empty list
* append an element to a list
* display number of elements in a list
* display specific elements of a list
* display last element of a list
* iterate over a list
* create a list of mixed element types
* create a list of lists
* display specific elements of a list of lists
* display number of elements in a list inside a list
* display specific elements of a list inside a list
* iterate over a list of lists

#### 

Keep a log of all transactions and list them using 't' op.

* list data structure and list of lists
* empty list literal
* append to a list
* iterate over a list
* get size of list
* for loop
* format field width

#### 
starting and running balance with transactions.

* list assignment to variables (spread?)
* format string field
* format field left alignment
* tuple as operand for format operator
* use of second variable to save initial value

#### 
Get starting account balance from command line argument, including error handling.

* module import and the sys module
* access to program arguments

#### 
Eliminate global variable by passing around balance.

* avoid globals by passing variables
* keep global space unpolluted

#### 
Create Account class with static balance member instead of passing around.

* class definition
* static (class) members and access to them
* variable and method members
* another way to avoid globals

#### 
Make balance an instance member and instantiate the class.

* class instantiation
* objects and object-oriented programming
* the class constructor
* instance members and access to them
* the self reference
* passing objects as parameters

#### 
Use float for amounts instead of int; update error checking and output format.

* float literal
* string conversion to float
* format float field
* format field precision
* prevent accumulation error
* the regular expression module and re pattern matching
* raise an exception
* distinguish different types of exception (ValueError, Exception)
* how diligent you must be with floats

#### 

Clean up and refactor more.

* more refactoring
* re-raise an exception

#### 
Add name to account, create multiple instances of account and test transactions.

* testing
* instrumenting code to assist with testing
* multiple instantiation of a class
* default parameter value
* program startup flag
* program exit code

automate from the command line, for example:
* printf "w\n.02\nd\n125.32\nw\n100\nd\n1\nt\nq\n" | ./lesson-25.py 100.01; echo

#### 
Use set to validate op.

* set data structure and set inclusion
* string expansion


Floating Point Calculations
---------------------------

The file `float_error/test.py` is included to demonstrate the challenges of floating point
calculations.  The file `float_error/output.txt` contains the output of running this.

