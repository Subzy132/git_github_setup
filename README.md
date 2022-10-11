# Python Intro

In week 2 we started working on python. We had to start by downloading python and then downloading pycharm as our IDE.
## Why python?

Easy to Use. Python has a simple syntax and hence is easy to understand and learn. Thus, making it a popular pick when it comes to programming languages.

## Python use cases

- Python Developer
- Software Development
- Automation
- Web Development
- Game Development
- Big Data 
- Artificial Intelligence 
- Data Science

## What's the benefits 

- Easy to Learn and Use
- Mature and Supportive Python Community
- Support from Renowned Corporate Sponsors
- Hundreds of Python Libraries and Frameworks
- Versatility, Efficiency, Reliability, and Speed
- Big data, Machine Learning and Cloud Computing
- First-choice Language
- The Flexibility of Python Language
- Use of python in academics
- It is interpreted

### variables
Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.

``` python
first_name = "Subhaan"
last_name = "Hussain"
salary = 50
travel = 3.5
```
### Data types

In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

- Text Type:	str
- Numeric Types:	int, float, complex
- Sequence Types:	list, tuple, range
- Mapping Type:	dict
- Set Types:	set, frozenset
- Boolean Type:	bool
- Binary Types:	bytes, bytearray, memoryview
- None Type:	NoneType
### Task

``` python
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

```


### setting up git and github using ssh key

1 - Generate ssh key-pair on localhost
2 - keep the private key on local host inside .ssh folder
3 - copy the public key into your repository on github

#### generating ssh key

1 - Open terminal 
2 - Enter Command ssh-keygen -t rsa -b 4096 -c "your email"

3 - Enter the file you wish to save the key

4 - Enter your passphrase twice

5 - Your identification is now saved

6 - once you have now set up your README.md file you now need to carry out the following commands

````
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin "git@github.com:[username]/[repository].git"
git push -u origin main
````

#### Git and Github
- add changes to our Git-Hub repo - the changes that we made on local host
- `git add filename` or `git add .` . means push everything from current location
- `git commit -m "new markdown added"` quotations marks needs to have logical meaning
- Now you need send this new data to github 
- `git push -u origin main` 
- `git status`
<<<<<<< HEAD
- add `.gitignore` file and then add all the dependencies you don't want commited to github
- If you have made changes on Git Hub then before adding on your local machine you need to pull whatever changes you made online and then commit your local machine.
- to pull changes from git-hub ``git pull``
=======

#### changes on github
