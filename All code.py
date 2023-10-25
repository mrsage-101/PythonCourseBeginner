

age = 21
print(age)

# here we need type casting, bcz cannot add numbers to string directly
print("You are " + str(age) + " years old")
print("You are ", age, " years old")
# f-string   
print(f"You are {age} years old")

# 4 basic datatypes
#integer
age = 21
players = 2
quantity = 5

print(f"You are {age} years old")
print(f"There are {players} online")
print(f"You would like to buy {quantity} items")

#float
gpa = 2.64
distance = 2.5
price = 10.99
print(f"Your gpa is {gpa}")
print(f"You distance is {distance}")
print(f"The price is {price}")

#string - series of characters with in quotes (quaotes can '' or "")
name = "Bro"
food = "pizza"
email = "abubaakryourkey309@gmail.com"
print(f"My name is {name}")
print(f"Your fav food is {food}")
print(f"Your email is {email}")

#Boolean
online = True
for_sale = False
running = False

print(f"Are u online? : {online}")
print(f"Is this for sale: {for_sale}")
print(f"Game running: {running}")

if running:
    print("The game is running")
else:
    print(f"Game is running: {running}")


# typecasting - converting a value of one data type into another data type
name = "Abubakar"
gpa = 2.64
age = 18 
student = True

type(name)
print(type(name))
print(type(gpa))
print(type(age))
print(type(student))

#explicit typecasting - manually converting the value of variable into different data type
# if the string is empty it will be false in bool
#age = bool(age)
#print(age)
#age = float(age)
#print(age)
#gpa = int(gpa)
#print(gpa)

#student = str(student)
#print(student)


#age = bool(age)
#print(age)

#implicit typecasting - automatically converting the data type of the variable
x = 2
y = 2.6

x = x/y
print(x)

x = True
print(x)

name = input("Enter your name: ")
age = input("Enter the age: ")
age = int(age)
age = age + 1
print(f"{name}'s  Age is : {age}")
print(name)

# mad libs game - user will submit noun,adj,verbs - input
adjective = input("Enter the adjective one: ")
noun = input("Enter the noun: ")
adj1 = input("Enter the adj1: ")
verb =  input("Enter the verb: ")

print(f"I study in a {adjective} class.")
print(f"I attended concert of {noun}.")
print(f"{noun} is {adj1}, and {verb}ing")

# cal area of rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width
print(f"The area is : {area}cm^2")

# shopping cart
item = input("What would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity
print(f"You have bought the {quantity} x {item}/s")
print(f"Your total is: {total}")

# arithmetic operators
friends = 10
friends = friends + 1
#friends *= 3
#friends = friends ** 2
#friends = friends % 3
print(friends)

# built-in math related functions
x = 3.14
y = -4
z = 5

#result = round(x,1)
result = abs(y)
result = pow(4,3)
result = max(x,y,z)
print(result)
result = min(x,y,z)
print(result)

import math
print(math.pi)
print(math.e)
x = 9
result = math.sqrt(x)
result = math.ceil(x)  # round the number up 9.5 will 10
print(result)
result = math.floor(x) # round down - 9.9 to 9.0
print(result)

#radius, circumference, area
import math

radius = int(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
print(f"The circumference is: {round(circumference, 2)}cm")
area = math.pi * pow(radius,2)
print(f"The area of the circle is: {area}cm^2")

#hypotenous of the right triangle
import math

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a,2) + pow(b,2))

print(f"Side C = {c}")


#if-statement - remeber order of your if conditions matters the most
age = int(input("Enter your age: "))
if age >= 18:
    print("You're now signed up!")
elif age < 0:
    print("Your age is not valid")
else:
    print("You're logged out")

# another example

response = input("Would you like food? (Y/N): ")

if response == "Y":
    print("Have some food:!")
elif response == "":
    print("You didn't typed anything")
else:
    print("No food for you!")

# dealing with boolean
for_sale = True
if for_sale:
    print("This item is for_sale")
else:
    print("This item is not for sale") 

# calculator program

operator_choice = input("Enter operator (+, -, *, /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator_choice == "+":
    add = num1 + num2
    print(f"Addtion result of {num1} + {num2}: {add}")
elif operator_choice == "-":
    sub = num1 - num2
    print(f"Subtraction result of {num1} + {num2}: {sub}")
elif operator_choice == "*":
    mul = num1 * num2
    print(f"Multiplication result of {num1} * {num2}: {mul}")
elif operator_choice == "/":
    div = num1 / num2
    print(f"Division result of {num1} / {num2}: {div}")
else:
    print("You choose not the mentioned operator")

# temperature covertor
unit = input("Is thish temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9*temp)/5+32,1)
    print(f"The temperature in Fahrenheit is: {temp} F")
elif unit == "F":
    temp = round((temp - 32) * 5/9,1)
    print(f"The temperature in Celsius is: {temp} C")
else: 
    print(f"{unit} is an invalid unit of measurement")

# logical operators and, or, not (it will change, if true then false,and false then true)
temp = 25
# and
temp = int(input("Enter the temperature: "))

if temp > 0 and temp < 30:
    print("The temperature is good!")
else:
    print("The temperature is bad")

# or
temp = int(input("Enter the temperature: "))
if temp < 0 or temp >= 30:
    print("The temperature is bad")
else:
    print("The temperature is good in between")

# not
sunny = True

if not sunny: # changes the true to false, and false to true
    print("Don't play cricket outside")
else:
    print("Play cricket outside")

# useful string methods
name = input("Enter your full name: ")

result1 = len(name)
# first occurrence
result2 = name.find(" ")
# last occurrence
result3 = name.rfind("a")
# capitalize - the first char of the string
result4 = name.capitalize()
# UPPER will capitalize the whole string
result5 = name.upper()
# Lower
result6 = name.lower()
# isdigit
result7 =  name.isdigit()
# isalpha
name = input("Enter your full name: ")
result8 = name.isalpha()
print(result8) 
# count
phone = input("Enter your phone number: ")
result8 = phone.count("-")
print(result8) 

#exercise abubakar siddique
# username should be less than 16 char, no spaces, no digits
username = input("Enter the username: ")
if len(username) > 16:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("You username doesnot contain spaces")
elif username.isalpha() == False:
    print("Your username cannot contain the digits")
else:
    print(f"Username : {username}")

# string indexer
# indexing [start:end:step]
credit_number = "1234-5678-9012-3456"
last_four = credit_number[-4:]
print(last_four)
reverse = credit_number[::-1]
print(f"the reverse credit numbber: {reverse}")

print(credit_number[0:4]) # 0 will be inclusive, and 4 will be exclusive
print(credit_number[5:9])
print(credit_number[5:19])
print(credit_number[-3])
# first will be inclusive - 1-3-(-)-6 ..... every second element
print(credit_number[ : :3])


# email slicer indexer
email = input("Enter your email: ")
index = email.index("@")
username = email[0:index]
domain = email[index:]

print(f"Username: {username} - index : {index} - domain: {domain}")

