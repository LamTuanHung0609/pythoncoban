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
Casting: Converting one data type to another data type. We use int(), float(), str(), list, set When we do arithmetic operations string numbers should be first converted to int or float otherwise it will return an error. If we concatenate a number with a string, the number should be first converted to a string. We will talk about concatenation in String section.
```
# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.99
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
num_float = float(num_str)  # Convert the string to a float first
num_int = int(num_float)    # Then convert the float to an integer
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6
num_int = int(num_float)
print('num_int', int(num_int))      # 10

# str to list
first_name = 'Hung'
print(first_name)               # 'Hung'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['H','u','n','g']

**Level 1**
3.Declare a first name variable and assign a value to it
4.Declare a last name variable and assign a value to it
5.Declare a full name variable and assign a value to it
6.Declare a country variable and assign a value to it
7.Declare a city variable and assign a value to it
8.Declare an age variable and assign a value to it
9.Declare a year variable and assign a value to it
10.Declare a variable is_married and assign a value to it
11.Declare a variable is_true and assign a value to it
12.Declare a variable is_light_on and assign a value to it
13.Declare multiple variable on one line
**Level 2**
1.Check the data type of all your variables using type() built-in function
2.Using the len() built-in function, find the length of your first name
3.Compare the length of your first name and your last name
4.Declare 5 as num_one and 4 as num_two
5.Add num_one and num_two and assign the value to a variable total
6.Subtract num_two from num_one and assign the value to a variable diff
7.Multiply num_two and num_one and assign the value to a variable product
8.Divide num_one by num_two and assign the value to a variable division
9.Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
10.Calculate num_one to the power of num_two and assign the value to a variable exp
11.Find floor division of num_one by num_two and assign the value to a variable floor_division
12.The radius of a circle is 30 meters.
13.Calculate the area of a circle and assign the value to a variable name of area_of_circle
14.Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
15.Take radius as user input and calculate the area.
16.Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
17.Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords


