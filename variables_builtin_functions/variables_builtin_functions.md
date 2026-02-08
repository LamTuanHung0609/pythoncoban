Variables: 
Python Variable Name Rules
+ A variable name must start with a letter or the underscore character
+ A variable name cannot start with a number
+ A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
+ Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables)

I will use standard Python variable naming style which has been adopted by many Python developers. Python developers use snake case variable naming convention. We use underscore character after each word for a variable containing more than one word. The example below is an example of standard naming of variables, underscore is required when the variable name is more than one word.

When I assign a certain data type to a variable, it is called variable declaration. The equal sign is an assignment operator. Assigning means storing data in the variable. The equal sign in Python is not equality as in Mathematics.

Example: 
```
fisrt_name = 'Hung'
middle_name = 'Tuan'
last_name = 'Lam"
country = 'Viet Nam"
age = "19"
skills = [Python, Java, SQL]
```

Let us use the print() and len() built-in functions. 
len () used to count the number of elements in an object.
```
name = "Hung"
print(len(name))
```
The result is: 4
```
text = "Hello World"
print(len(text))  
```
The result is: 11
*Note: Spaces are also counted as characters.

Multiple variables can also be declared in one line.
```
first_name, last_name, country, age = 'Hung', 'Lam', 'Viet Nam', '19'
print ('First Name:', first_name)
print ('Last Name:', last_name)
print ('Age:', age)
print ('Country:', country)
```
Getting user input using the input() built-in function.
```
first_name = input('What is your name: ')
age = input('How old are you? ')

print('First Name:',first_name)
print('Age:',age)
```
