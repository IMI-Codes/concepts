import re

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
