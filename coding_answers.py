########## Question 2 ####################
#Write a function that can define whether a word is a Palindrome or not
def is_it_Palindrome(word):
  try:
    if word == word[::-1]: #checking if reverse of word is read the same as the original
      print('Yes, this is a palindrome')
      return True
    else:
      print('No, this is not a palindrome')
      return False
  except:
    raise ValueError('The given word is not a string')

########## Question 3 ####################
#Write tests for the newly created Palindrome function.
import unittest
#import functions from file
class TestPalindrome(unittest.TestCase):
  def test_is_it_Palindrome(self):
    #these will test if the is_it_Palindrome function correctly returns a True or False when given a word
    self.assertEqual(is_it_Palindrome('racecar'), True)
    self.assertEqual(is_it_Palindrome('madam'), True)
    self.assertEqual(is_it_Palindrome('nah'), False)
    self.assertEqual(is_it_Palindrome('possibly'), True) #testing a bad case

  def test_is_error_raised(self):
    #these will test if a valueerror is correctly raised when integers are assigned to the word parameter- only words should be tested
    self.assertRaises(ValueError, is_it_Palindrome(123), True)
    self.assertRaises(ValueError, is_it_Palindrome(56), True)

########## Question 9 ####################
def two_number_sum(array, target): #test every pair
  for i in range(len(array)): #iterate through 'i'ndex in array
    for s in range(i + 1, len(array)): # 's'econd'- starting from the following number to see pair
      if array[i] + array[s] == target: #checking if the sum of a pair is equal to the target value
          #print([array[i], array[s]])
          return [array[i], array[s]] #returns the values at each index if condition met
  else:
    return[] # if condition not met after iterations, returns empty array

#testing function
my_numbers = [3, 5, -4, 8, 11, 1, -1, 6]
target_sum= 10 # output is [11, -1]

my_numbers2 = [5, 9, -4, 2, 3, 2, -1, 6]
target_sum2 = 13 #output is []

result= two_number_sum(my_numbers, target_sum)
print(result)