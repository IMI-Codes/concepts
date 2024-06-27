myList = [2,'Name',3.2]
#list AKA Array

Hobbies = []
Hobbies.append('Running')
Hobbies.append('Boxing')
Hobbies.append('Watching Movies')
Hobbies.append('Strength Training')
#in operator

check = 'Running' in Hobbies

for hobby in range(len(Hobbies)):
  """ print(hobby) """#this will just return the index
  """ print(Hobbies[hobby]) """
  print(f"The Index for {Hobbies[hobby]} is {hobby}")
  
#range return does need the length to be subtracted by 1 why? 
#it implicitly  subtracts one from the index so there is no need to subtract on

# + operator on list concatenates two lists 

firstThree = [1,2,3]
secondThree = [4,5,6]
mergedThree = firstThree + secondThree


# * repeats a given list

mulitiplied = firstThree * 2

#list slices

test = mulitiplied[2:len(mulitiplied)-1]
wholeArray = mulitiplied[:]

girls = ['Wunika','Ellen','Nanchin','Fafa']
boys = ['Seth','Manasseh','Ola','Emeka','Austin']

boys.extend(girls)
print(boys)
boys.sort()

boys.pop(-4)
del boys[-1]
boys.remove('Fafa')

nums = [300000,3000000000,188888,3534543]

maximum = max(nums)
minimum = min(nums)
numberOfElements = len(nums)
total = sum(nums)
average = total/numberOfElements

numlist = list()

#converting a string to a list
myName = 'Manasseh'
letters = list(myName)
print(letters)


sentence = "Hello I'm Manasseh Nice to Meet you"
words = sentence.split()

email = 'somerandomemail@emailclient.com'
parasedEmail = email.split('@')


#join method
param = ' '
reverted = param.join(parasedEmail)

#parsing lines
