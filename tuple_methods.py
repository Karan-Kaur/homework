# Section 4: Python tuple methods- describe each method and provide an example

#count()- this method returns the number of times a given value appears within a tuple.
alphabet = ('a', 'b', 'a', 'c', 'd', 'e')
alphabet2 = alphabet.count('a')
print(alphabet2) #returns 2

#index()- this method returns the index/position of the given value, provided that it is in the tuple (if not, a ValueError exception is raised.)
# A user can also specify the positions they wish to search through the optional start and end parameters.
numbers = (1, 2, 3, 4, 5, 6)
num_where = numbers.index(4)
print(num_where) #returns 3