""" userInput = ''' 
This will show up as multiple lines of a string
Well dang
'''

import json

data = '''
[{'name':'Manasseh', 'id':'200','x':"too many"},{'name':'Bruce Wayne','id':'399','x':'That Nigga a hoe'}]
'''

info = json.loads(data)
print('user count:',len(info)) """

