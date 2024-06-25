#functions
#built in functions
import math
import random
max('Hello World')
#max returns the largest character in a string
min('Hello World')
#min returns the smallest character in a string

len('Hello World')
#len returns the length of a string AKA the number of characters

#type conversion functions
int('32')

int(3.99999)

int(-2.3)

float(32)

float('3.2345')

str(52)

str(3.14159)

math.sin(90)
math.log10(1)
math.pi

for i in range(10):
  x = round(random.random()*10)
  print(x)
  
random.randint(5,10)

random.randint(5,10)

t = [1,2,3]
random.choice(t)

def greet(name):
  return "Hello",name

print(greet)
print(type(greet))

print(math.pow(5,2))
print(round(math.sqrt(25)))
print(greet('Manasseh'))