# What are python Variables?
# To store any Data
# To store User Data - hard code the data - any other types
# first_name = "Angel" - String
# name = "Subhaan"
# DOB = 99 - Integer
# UK_resident = True or False - Boolean
# salary = 400000 - Integer
# travel = 15.4 - Float
# gross_salary = salary + travel

print('Hello world!')

first_name = "Subhaan"
last_name = "Hussain"
salary = 50
travel = 3.5
print(first_name)
print(last_name)
print(salary)
print(travel)

# How to find out the type of data stored in the var
# type ()
print(type(travel))

# interact with the user by taking in user data - input()

print('Good Morning, Please enter your name.')

name = input('Enter name: ')
print("Hello " + name)

userfname = input('Please enter your first name: ')
userlname = input('Please enter your last name: ')
user_dob = input('please enter your Date of birth: ')
user_course = input('Please enter your course name: ')
user_resident = input('Please enter if you are a uk resident or not (Yes or No): ')

print(userfname)
print(userlname)
print(user_dob)
print(user_course)
print(user_resident)