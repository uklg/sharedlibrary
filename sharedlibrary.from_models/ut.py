#!/usr/bin/python3
import unittest

# This is the class we want to test. So, we need to import it
import Person as PersonClass

class Test(unittest.TestCase):
  """
  The basic class that inherits unittest.TestCase
  """
  person = PersonClass.Person() # Instaniate the Person Class
  user_id = [] # variable that stores obtained user_id
  user_name =  [] # variable that stores person name

  # test case function to check the Person.set name function
  def test_0_set_name(self):
    print("Start set_name test\n")
    """
    Any method which starts with ``test_`` will be considered a test case.
    """
    for i in range(4):
      # initialise a name
      name = 'name'+str(i)
      # store the name into the list variable
      self.user_name.append(name)
      # get the user id obtained from this function
      user_id=self.person.set_name(name)
      # check if the obtained  user id is null or not
      self.assertIsNotNone(user_id) # null user id will fail the test
      # store the user id in the list
      self.user_id.append(user_id)
    
      print("user_id length = ", len(self.user_id))
      print(self.user_id)
      print("user_name length = ", len(self.user_name))
      print(self.user_name)
      print("\nFinish set_name test\n")


  # test case function to check the Person.get_name function
  def test_1_get_name(self):
    print("Start get_name test\n")
    """
    Any method that starts with ``test`` will be considered a test case.
    """
    length = len(self.user_id) # total number of stored user information
    print("user_id length = ",len(self.user_name))
    for i in range(6):
      # if i not exceed total length then verify the returned name
      if i < length:
        # if the two name not matches it will fail the test case
        self.assertEqual(self.user_name[i], self.person.get_name(self.user_id[i]))
      else:
        print("Testing for get_name no longer test")
        # ' if length exceeds then chech the 'no such user message'  type  message 
        self.assertEqual('There is no such user', self.person.get_name(i))
      print("\nFinish get_name test\n")

if __name__ == "__main__":
  # begin the unittest.main()
  unittest.main()
