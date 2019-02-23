# password-validation-module
A Python3 script to validate the password proposed by the user.

A certain system needs a password validator module, which upon receiving a string with a password and a list with the requirements of this password, returns whether the password is valid or not. The list of the password requirements is composed of tuples containing the following: 

• First value:
  * LEN – password length
  * LETTERS – # of letters
  * NUMBERS – # of numbers
  * SPECIALS – # of special characters

• Second value: <, > or =

• Third value: an integer number

Ex.:
req = [(‘LEN’, ‘=’, 8), (‘SPECIALS’, ‘>’, 1)]

req specify a password with eight characters and at least two special characters.


System buillt using only Python3 and no external packages.
