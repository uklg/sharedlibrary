#!/usr/bin/python3

import SharedLibrary

parseline=SharedLibrary.ParseLine()

port=parseline.get_accessport()

#print(port)




turl=SharedLibrary.TestURL()
url=turl.get_url(8003)

"""
'http://127.0.0.1:8003'
"""


response=turl.get_response(url)




reply=turl.check_return_code(response[0])

print(reply)


r1= turl.caseless_match('nextArrow',response[1])

print(r1)



# something that should fail

r2= turl.caseless_match('nextArrownotger',response[1])
print(r2)


turl.print_summary()

#turl.execute()


print ( turl.test_endpoint('nextArrow') )


#print ( turl.test_endpoint(url='https://www.google.com','nextArrow34') )

