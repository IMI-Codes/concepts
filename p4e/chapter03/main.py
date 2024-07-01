# == is equal to 
x = 5
y = 6
5 == 5
5 == 6 

# !=
print(x > y) # x greater than y
print(x < y) # x less than y
print(x >= y) # x greater than or equal to y 
print(x <= y) # x less than or equal to y
print(x is x) # X is the same as x
print(x is not y) # x is not the same as y


#True and False are keywords in python
print(type(True))
print(type(False))

#Logical operators
#and or not

#conditional execution
if x > 1:
  print('Yes')

# pass serves a placeholder
if x < 1:
  pass

#else
if x > 1 and x < 100:
  print('valid')
else:
  print('Nahh')
  

if x < 20 and x%2 == 0:
  print('yeah valid')
elif x < 10:
  if x > 10:
    print('No Brodie')
  elif x != 5:
    print('nope')
elif x != 10:
  print("bro c'mon")
  
  
inp = input('Enter Fahrenheit Temperature:')
try:
  fahr = float(inp)
  cel = (fahr - 32.0) * 5.0 / 9.0
  print(cel)
except:
  print('Please enter a number')