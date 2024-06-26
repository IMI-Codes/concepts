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

