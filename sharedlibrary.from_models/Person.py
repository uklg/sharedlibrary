#!/usr/bin/python3

class Person:
  name=[]

  def set_name(self, user_name):
    self.name.append(user_name)
    return len(self.name) -1
    # test use case failure use this instead:
    # return None

  def get_name(self, user_id):
    if user_id >=  len(self.name):
      return 'There is no such user'

    else:
      return self.name[user_id]
      #return 'some other text to test test failure'
      

def richtest():


  person = Person()
  r=person.set_name('John')
  print(r)
  r=person.set_name('Paul')
  print(r)
  print(person.name)
  print(person.get_name(0))
  print(person.get_name(1))
  #print(person.user_id)


if __name__ == '__main__':
  person=Person()
  print('User Abbas has been added with id', person.set_name('Abbas'))
  print('User associated with id 0 is', person.get_name(0)) 
