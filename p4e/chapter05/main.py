""" x = 0
x = x + 1
print(x) """

#while loop
""" n = 5
while n > 0:
  print(n)
  n = n - 1
print('BlastOff')

while True:
  line = input('>\n')
  if line == 'done':
    break
  print('yeah',line)

while True:
  line = input('>')
  if line[0] == '#':
    continue
  if line == 'done':
    break
  print(line)
print('Done')
 """
#for loop




""" friends = ['Seth','Bobbie','Austin']
for friend in friends:
  print(friend) """


#list AKA array []

#counting and summing


""" sum = 0
for number in numbers:
  sum = sum + int(number)
print(sum) """

numbers = ['22','32','37','38','100']


actualNumbers = []
for number in numbers:
  convertedNumber = int(number)
  actualNumbers.append(convertedNumber)
  
print(actualNumbers)


largestSoFar = None

for numerals in actualNumbers:
  if largestSoFar is None or numerals > largestSoFar:
    largestSoFar = numerals
  print('Current Number:',numerals, 'Largest Number So Far:',largestSoFar)
print('The Largest Number is:', largestSoFar)

#final