# Section 3: Python list methods- describe each method and provide an example
#1) append() - this method adds an additional item to a list as a singular element, regardless of its data type (i.e. string, integers etc)
methods = ['string', 'list', 'dictionary']
methods.append('tuple') #adds tuple to the list
print(methods)

#2) clear() - this method removes all the items currently held within a list.
methods = ['string', 'list', 'dictionary', 'tuple']
methods.clear()
print(methods)

#3) copy() - this method creates a copy/duplicate of an existing list (in its current state.)
methods = ['string', 'list', 'dictionary', 'tuple']
methods2 = methods.copy() #created a new list which is a duplicate
print(methods2)

#4) count() - this method returns a count of the number of times a given item/object/value appears in a list.
marks = [4, 6, 11, 6, 3, 4]
mark_no = marks.count(4)
print(mark_no) #returns 2

#5) extend() - Alike append(), this method also adds items to a list but only accepts iterables and adds each item as individual elements rather than a singular one.
methods = ['string', 'list', 'dictionary', 'tuple']
more_methods = ['set', 'file']
methods.extend(more_methods)
print(methods)

#6) index() - this method returns the index/position of a given item within a list (only the first time it appears.)
methods = ['string', 'list', 'dictionary', 'tuple', 'set', 'file']
position = methods.index('dictionary')
print(position) # return 2

#7) insert() - this method inserts an item at a specified position/index within a list.
methods = ['string', 'list', 'dictionary', 'tuple', 'set', 'file']
methods.insert(2, 'another method')
print(methods)

#8) pop() - this method removes an item at a specified position/index within a list (the argument is the index)
methods = ['string', 'list', 'another method', 'dictionary', 'tuple', 'set', 'file']
methods.pop(2)
print(methods)

#9) remove() - this method removes the first appearance of a specified element within a list.
methods = ['string', 'list', 'another method', 'dictionary', 'tuple', 'set', 'file']
methods.remove('another method')
print(methods)

#10) reverse() - this method reverses the order of the items in a list.
methods = ['string', 'list', 'dictionary', 'tuple', 'set', 'file']
methods.reverse()
print(methods)

#11) sort() - this method sorts items of a list by a given criteria. By default, it will be ascending (alphabetically for strings, by number for integers)
# but the method allows for key parameters (e.g. len- will sort the items by length of item) or reverse (if set to true, this will sort the items in descending order)
methods = ['string', 'list', 'dictionary', 'tuple', 'set', 'file']
methods.sort() #would sort items alphabetically, ascending order.
methods.sort(reverse=True) #sort items alphabetically, descending order.
methods.sort(key=len) #sorts according to length of the words, asc. e.g. set at pos 0.