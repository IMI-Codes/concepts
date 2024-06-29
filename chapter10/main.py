""" alphabets = 'a','b','c','d','e','f'
 """#or another representation of tuples

""" someData = (1,2,['JJK','Baki','Demon Slayer'],{'name':'Kaiju No.8'})

t1 = (4,)

aWord = ('name')  """#this is string not a tuple always put a comma at the end if you want to make it a tuple also tuples are like strings they are immutable


#another way to create a tuple
""" mytuple = tuple()

print(type(mytuple)) """

#turning a string into a tuple
""" name = "Manasseh"
lowerCaseName = name.lower()
convertedMyName = tuple(lowerCaseName)
print(convertedMyName)
print(f'This is a {type(convertedMyName)} {convertedMyName}') """

#most list operation work on tuples
""" print(len(convertedMyName))
print(convertedMyName[0])
print(convertedMyName[0:4])
 """

#comparing tuples


""" numberTuple = 1,2,3,4
secondTuple = 5,6,7,8

print(numberTuple < secondTuple)

txt = 'but soft what light in yonder window breaks' """
""" words = txt.split()
t = list()
for word in words:
  t.append((len(word), word))
  
t.sort(reverse=True)
  
print(t)

res = list()

for length, word in t:
  res.append(word)
  
print(res) """

#Tuple Assignment

#This will still work with brackets on the left side of the assignment statment
""" fullName = ('Ishima','Manasseh','Ishima')
 """
""" firstName,middleName,lastName = fullName

print(firstName)

hobbies = ['Resistance Training','Running','Reading','Coding'] """

""" nonContact,Cardio,mind,skill = hobbies

print(nonContact) """


""" warrior = 'Baki'
mage = 'Crimson' """
#easily swap variable values
""" (warrior,mage) = (mage,warrior)

print(mage) """

""" email =  "bruewayne@gmail.com"
uname,domain = email.split('@')
print(uname)
print(domain) """


#Dictionaries and Tuples

""" KaijuRatings = {'NO.8':9.8,"NO.9":10,'NO.1':8.3}
 """""" ratingList = list(KaijuRatings.items())
ratingList.sort()
print(ratingList) """

""" for kaijuName,Rating in KaijuRatings.items():
  print(f"Kaiju {kaijuName} has a Rating of {Rating}")  """
  
  

characters = {'Baki':'Grappler','Gojo':'Strongest Soccercer','Kaiju NO.8':'Strongest Kaiju'}


arr = list()

for character,stat in characters.items():
  arr.append((character,stat))
  arr.sort(reverse=True)
print(arr)

#using tuples as keys in dictionaries
#intriguing
directory = dict()
first = 'Ishima'
last = 'Manasseh'
number = '1234567908'

map = (first,last) 
directory[last,first] = number
print(directory)


#List Comprehension

list_of_ints_in_strings = ['42', '65', '12']
list_of_ints = []
for x in list_of_ints_in_strings:
  list_of_ints.append(int(x))
print(sum(list_of_ints))

#a more compact version of the above code 
list_of_ints_in_strings = ['42', '65', '12']
list_of_ints = [ int(x) for x in list_of_ints_in_strings ]
print(sum(list_of_ints))
