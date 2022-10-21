#!/usr/bin/python3


import urllib.request


fd=open('build','r')
lines=fd.readlines()
fd.close()


ACCESSPORT=None

for l in lines:
  if 'accessport=' in l:
    ACCESSPORT=(l.split('=')[-1].strip())
    
print(ACCESSPORT)


errors=0
tests=0

URL="http://127.0.0.1:%s" % ACCESSPORT

print(URL)

response=urllib.request.urlopen(URL)


#help(response)


code=response.getcode()

if code !=200:
  print('error code not 200')
  errors +=1


responselines=response.read()


def caseless_match(searchstring,contenttosearch):
  if searchstring.casefold() in str(contenttosearch).casefold():
    return True
  else:
    return False


if not caseless_match('nextArrow',responselines):
  print('Cannot find string')
  errors +=1

if not caseless_match('Professional wedding DJ',responselines):
  print('Cannot find string')
  errors +=1

print("This is a test that checks certain http requests are correct")
print("errors: %s" % errors )
#print("total errors: %s out of %s" % len(errors))



