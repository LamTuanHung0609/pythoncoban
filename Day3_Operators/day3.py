#Declare your age as integer variable
#Declare your height as a float variable
#Declare a variable that store a complex number
```
age = 19  #int
height = 1.81 #float 
a_complex = j + 22i 
```

#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
```
base = float(input('a: '))
height = float(input('h: '))
area = 0.5 * base * height
print ('The area of the triangle is: ', area)
```

#Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
```
a = float(input('enter side a: '))
b = float(input('enter side b: '))
c = float(input('enter side c: '))
perimeter = a + b + c
print ('The perimeter of the triangle is: ', perimeter)
```
#Write a piece of code that prompts the user to enter a year. Calculate the number of seconds corresponding to that year.
```
year = int(input('enter a year: '))
x = year * 365 * 24 * 3600 
print ('The corresponding number of seconds is: ', x)
```
#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width)) Get radius of a circle using prompt.
```
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width
perimeter = 2 * (length + width)

print("Area of the rectangle:", area)
print("Perimeter of the rectangle:", perimeter)

radius = float(input("Enter radius: "))
print("Radius of the circle:", radius)
```
#Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
```
r = float(input('Enter the radius: '))
pi = 3.14
area = pi * r * r
circumference = 2 * pi * r 
print ('The area is: ', area)
print ('The circumference is: ', circumference)
```
#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
```
y = x**2 + 6*x + 9
x = input('Enter x: ')
print ('y')
``` 
#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
```
len_python = len("python")
len_dragon = len("dragon")

print(len_python)
print(len_dragon)
prin(len_python > len_dragon)
```
#Use and operator to check if 'on' is found in both 'python' and 'dragon'
```
print('on' in 'python' and 'on' in 'dragon')
```
#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
```
a = int(input('enter a number: '))
print (a%2 == 0)
```
#Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
```
hours = input('Enter hours: ')
rate = input('Enter rate: ')
pay = hours * rate 
print ('your pay is: ', pay)
```


