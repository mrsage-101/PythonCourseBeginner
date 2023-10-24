

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