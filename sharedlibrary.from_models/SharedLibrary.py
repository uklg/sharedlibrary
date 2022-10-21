#!/usr/bin/python3

# can share this by appending its path to anther app

import urllib.request


class ParseLine:


  def get_accessport(self,filetoparse='build'):

    fd=open(filetoparse,'r')
    lines=fd.readlines()
    fd.close()


    ACCESSPORT=None

    for l in lines:
      if 'accessport=' in l:
        ACCESSPORT=(l.split('=')[-1].strip())
    
    return(ACCESSPORT)


class TestURL:

  # This accumalates errors once the class is constructed
  errors=0
  tests=0


  def get_url(self,  port):

    self.URL="http://127.0.0.1:%s" % str(port)

    return self.URL



  def get_response(self,url):

    response=urllib.request.urlopen(url)
    #help(response)
    code=response.getcode()
    responselines=response.read()
    return [code,responselines]


 
  def check_return_code(self,code):
    if code !=200:
      print('error code not 200')
      return False
      self.errors +=1
    else:
      return True 





  def caseless_match(self,searchstring,contenttosearch):
    if searchstring.casefold() in str(contenttosearch).casefold():
      return True
    else:
      self.errors += 1
      return False


  def print_summary(self):
    print("This is a test that checks certain http requests are correct")
    print("errors: %s" % self.errors )
    #print("total errors: %s out of %s" % len(errors))

   # run the constructor
   # def __init(self, 


  def execute(self,port=8003):

    url=self.get_url(8003)
    print(url)
    responselines=self.get_response(url)[1]
    

    if not self.caseless_match('nextArrow',responselines):
      print('Cannot find string')
      self.errors +=1

    if not self.caseless_match('Professional wedding DJ',responselines):
      print('Cannot find string')
      self.errors +=1

    self.print_summary()


  def test_endpoint(self,matchstring):
    url=self.get_url(8003)
    responselines =  self.get_response(url)[1]
    responsecode  =  self.get_response(url)[0]

    stringmatch = self.caseless_match(matchstring,responselines)
    codematch   = self.check_return_code(responsecode) 
    rdict= { 'returncodegood': codematch, 
              'stringmatchgood':  stringmatch, 
              'responsecode': responsecode, 
              'url': url }
    
    self.print_summary()
    return rdict


#  if __name__ == '__main__':
#    main()


