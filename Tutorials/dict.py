# What is a Dictionary
# How to manage the dictionaries - How to manage the data using Dictionaries
# It works as a key value pair - Key = Value
# Syntax Lists = [] Dict = {} Tuples = ()
# Dict Syntax = {"name": "Sparta" ,      }
#                  0
# store student's data - name, course_name, progress, completed_lessons

student_1 = {
    "name": "Subhaan",
    "course_name": "Devops",
    "completed_lessons": 4,
    "completed_lessons_names" : ["lists", "tuples", "strings"]
}

print(student_1)
print(type(student_1)) # To show the data type
print(student_1["course_name"]) # This will dislay the value saved inside stream
print(student_1["completed_lessons_names"]) # prints the full list under Completed_lessons_names
print(student_1["completed_lessons_names"][0]) # Prints the value in index 0 under the completed lessons names lists
student_1["completed_lessons"] = 3 # Changing the value of a key
print(student_1["completed_lessons"])

# Delete an item from the list of completed_lessons_names

student_1["completed_lessons_names"].remove("strings") # removing a value of a list within the dictionary
print(student_1["completed_lessons_names"])

# Dict Builtin Methods
# Display keys only or values
# .keys() .values()
print(student_1.keys())
print(student_1.values())
