# Dictionary basics task

# 1 - Define a dictionary call story1, it should have the followign keys:
        # 'start', 'middle' and 'end'

story1 = {
    "start": "There once was a kid called Subhaan, who lived in London and had gotten bit by a spider on a school trip",
    "middle": "He found out an evil doctor with 4 mechanical arms was planning on blowing up the earth and he had to stop him!",
    "end": "They fought and Subhaan managed to defeat him and save the world"
}


# 2 - Print the entire dictionary

print(story1)

# 3 - Print the type of your dictionary

print(type(story1))

# 4 - Print only the keys

print(story1.keys())

# 5 - print only the values

print(story1.values())

# 6 - print the individual values using the keys (individually, lots of printi commands)

print(story1["start"])
print(story1["middle"])
print(story1["end"])

# 7 - Now let's add a new key:value pair.
#     'hero': yourSuperHero

story1["hero"] = "Subhaan"
print(story1.keys())

