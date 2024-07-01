import re
fileHandle = open('mbox-short.txt')
for line in fileHandle:
  line = line.rstrip()
  if re.search("^From:.+@",line):
    print(line)


""" for line in fileHandle:
  line = line.rstrip()
  if re.search('^F..m:.+@',line):
    print(line) """


"""if re.search('^From:',line):print(line) """
""" if re.search('^F..m:',line):
      print(line) """
#character matching in regular expressions













# Search for lines that contain 'From'
""" import re
hand = open('mbox-short.txt')
for line in hand:
  line = line.rstrip()
if re.search('From:', line):
  print(line) """
  
  
#variation on the above code
""" import re
hand = open('mbox-short.txt')
for line in hand:
  line = line.rstrip()
if re.search('ˆFrom:', line):
  print(line) """
  
  
#character matching in regular expressions
