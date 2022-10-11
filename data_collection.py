# Data collection
# Lists
# Tuples
# Dict


# Lists
# Syntax ["asdf", "dafsa", "afdfdga"]

# apply DRY

shopping_list = ["ketchup", "fanta", "eggs", "bread"]
print(shopping_list)
print(type(shopping_list))
shopping_list.append("chicken")
shopping_list.pop(1)
shopping_list[2] = 'ice cream'
print(shopping_list)


# can list have multiple data types

multiple_types = [1, 2, 3, "one", "two", "three"]

print(multiple_types)

# Tuples
# Immutable - can't be changed - edited - added
# Syntax ("")

essentials = ("Milk", "Paracetemol", "drinks")
print(essentials)
print(type(essentials))
# whats the difference between lists and tuples
# essentials [0] = "coffee" - this will show up as an error
print(essentials)

x = 5
x = complex(x)

print(x)