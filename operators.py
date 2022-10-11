# Let's see the operators in action

### Intro to Data types & Operators

# - `+ - * / `

# ##### comparison Operators
# #
# # - `>` greater than
# # - `<` lesser than
# # - `==` True or False
# # - `>=` greater than or equals to
# # - `<=` Lesser than or equals to
#
# a = 24
# b = 15
#
# print(a + b) # outcome of a and b added = 39
# print(a - b) # outcome of a - b = 9
# print(a > b) # outcome boolean = True
# print(a == b) # outcome false because a does not equal b
# print(a % b) # outcome will be 9 because 24/15 is 1 remainder 9
# print(a != b) # outcome will be true because 24 doesn't equal 15
#
# # create a print statement to show the use case of it
#
# # boolean Builtin methods in Python - Boolean Methods
# # DRY - Do Not Repeat yourself
#
# greeting = "Hello World!"
#
# print("greeting = " + greeting)
# print(greeting.isalpha())
# print(greeting.islower())
# print(greeting.startswith("H"))
# print(greeting.endswith("!"))
# print(greeting.isdigit())
#
# # string slicing
#
# print(greeting)
#
# # we have builtin method that checks the len of string
#
# print(len(greeting))
# print(greeting[0:5])
# print(greeting[6:12])
#
# print(greeting[-12:-6])
# print(greeting[-6:])

# String Methods are available

# use var = string "afsafghjsjagkfds"

# white_space = "lot's of spaces at the end                "
#
# print(len(white_space))
# # strip() removes the spaces at the end of the string
# print(len(white_space.strip()))
#
# example_text = "here's some text with lot's of text"
#
# print(example_text.count("text"))
# print(example_text.upper())
# print(example_text.capitalize())
# print(example_text.replace("with", "that has"))

first_name = "Subhaan"
last_name = "Hussain"
salary = 40


print(first_name)
print(last_name)
print(first_name + " " + last_name + " and your salary is " + str(salary))
#F string
print(f"{first_name} {last_name} and your salary is {salary}")