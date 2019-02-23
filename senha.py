#!/usr/bin/env python
# coding: utf-8

# #### Problem Identification

#     A certain system needs a password validator module, which upon receiving a string with a
#     password and a list with the requirements of this password, returns whether the password is valid
#     or not. The list of the password requirements is composed of tuples containing the following:
# 
#     • First value:
#     o LEN – password length
#     o LETTERS – # of letters
#     o NUMBERS – # of numbers
#     o SPECIALS – # of special characters
#     • Second value: <, > or =
#     • Third value: an integer number
# 
#     Ex.:
#     req = [(‘LEN’, ‘=’, 8), (‘SPECIALS’, ‘>’, 1)]
#     req specify a password with eight characters and at least two special characters.
#     Write a Python 3 script to solve this problem and the unit test to validate it, without installing
#     external package


# #### Solution

# In[44]:


def get_operation(value, operator, requirement_value):
    if operator == '<':
        return value < requirement_value
    elif operator == '>':
        return value > requirement_value
    elif operator == '=':
        return value == requirement_value

def get_value(password, operation):
    if operation == 'LEN':
        return len(password)
    elif operation == 'LETTERS':
        return sum(char.isalpha() for char in password)
    elif operation == 'NUMBERS':
        return sum(char.isnumeric() for char in password)
    elif operation == 'SPECIALS':
        return sum((not(char.isalpha()) and not(char.isnumeric())) for char in password)

def validator(password, requirements):
    for operation, operator, requirement_value in requirements:
        value = get_value(password, operation)
        result = get_operation(value, operator, requirement_value)
        assert result, 'Password does not match the required format'
    print('Password accepted')


# #### Simple simulation exercise

# In[45]:


req = [('LEN', '=', 8), ('SPECIALS', '>', 1)]


# In[46]:


validator('123456!!', req)


# In[47]:


validator('1234567!', req)

