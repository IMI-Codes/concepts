""" fruit = 'apple'
print(fruit[0])
print(len(fruit))
print(fruit[-1])

for letter in fruit:
  print(letter)
  

name = 'Ishima Manasseh'
print(name[0:6])
print(name[:])
print(name[0:])
print(name[:1])


greeting = 'Whats up brodie'
newGreeting = "How's It going" + greeting[8:]

def counter(word,char):
  list = word 
  count = 0 
  for letter in word:
    if letter == char:
      count = count + 1
  return count  """

""" print(counter('Ishima Manasseh Ishima',''))
 """
""" print(dir(13))
print('\n')
print('\n')

print(dir('S'))
print('\n')
print('\n')

print(dir(3.33))
print('\n')
print('\n')

print(dir([3,2]))
print('\n')
print('\n')
 """

""" print(dir({name:'Manasseh'}))
 """
word = "Manasseh"
newWord = word.upper()

letterIndex = word.find('M')

sentence = ' Hello World  '
newSentence = sentence.strip()

myName = 'Manasseh'
print(myName.startswith('M')) 

print(myName.count('s'))

#find string method
print(myName.find('M'))


data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')

sppose = data.find(' ')

email = data[5:21]

camel = 42
print(type(f'{camel}'))#string literals

print(f'Hello Im Batmam Im {camel}')