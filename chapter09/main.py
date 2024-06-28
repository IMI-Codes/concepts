#dictionary AKA objects in Javascript

""" eng2sp = dict()
myObj = {'name':'Ishima Manasseh',"hobbies":['Running',"Strength Training","Reading Books"]}

eng2sp['one'] = 'uno'

anArr = myObj['hobbies'] 

totalElement = len(myObj)
#in operator 
isIn = 'name' in myObj

vals = list(myObj.values())

isThere = myObj.get('name',None)
word = 'brontosaurus'
d = dict()
for c in word:
  d[c] = d.get(c,0) + 1
print(d)
print(myObj) """


wordContainer = dict()
fileHandle = open('romeo.txt')

for line in fileHandle:
  line = line.lower()
  words = line.split()
  
  for word in  words:
    wordContainer[word] = wordContainer.get(word,0) + 1

""" largest = 0 
for key in wordContainer:
  if wordContainer[key] > largest:
    largest = wordContainer[key]
    
print(largest)
 """


lst = list(wordContainer.keys())
lst.sort()
print(lst)
for key in lst:
  print(key, wordContainer[key])
  
import string
print(string.punctuation)