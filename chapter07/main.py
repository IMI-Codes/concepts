#opening files
#fileHandle = open('data.txt')

#\n new line character

#reading files 
""" count = 0
for line in fileHandle:
  count = count + 1
print(count) """

""" fileData = fileHandle.read()
 """""" print(len(fileData)) """
""" print(fileData[:200])
 """
 
#searching through a file
""" for line in fileHandle:
  line = line.rstrip()
  if line.startswith(' '):
    print(line) 
for line in fileHandle:
  line = line.rstrip()
  if not line.startswith(' '):
    continue
  print(line)
  
  for line in fileHandle:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1: continue
    print(line)
     """
     
#Letting the user the choose a file

""" def extensionChecker(data):
  validate = data.find('.txt')
  if validate == -1:
    appended = data[0:] +'.txt'
    return appended
  elif validate != -1:
    validated = data
    return validated """

#please note that should try and except when opening files so incase you receive an invalid input you program can end gracefully

 
#writing files
#we pass an argument to the open function 'w'

""" fileHandle = open('data.txt','w') """ #note this will clear out the file if there is any data in it and if the file does not exist it creates it 

#someHandle.write('data.........') or someHandle.write(variable) this will return the length of the updated always end each line with the newline character(\n) 
#also when done writing remember to end with someHanlde.close() the same should apply for reading but we can be lazy here

#repr method

""" sentence = 'Domain Expansion: Infinite Void\n'
print(repr(sentence)) """

