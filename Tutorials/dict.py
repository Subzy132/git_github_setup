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
print(type(student_1))
print(student_1["course_name"]) # This will dislay the value saved inside stream
print(student_1["completed_lessons_names"])
print(student_1["completed_lessons_names"][0])
