#Section 5: Dictionary methods- describe each method and provide an example
#1) clear()- this method removes all the items from a dictionary
restaurants = {1:"Nandos",
            2: "Vietnamese Street Kitchen",
            3: "Jimmy Spices",
            4: "Turtle Bay",
            5: "Ed's Diner"}

restaurants.clear()
print(restaurants)

#2) copy()- this method returns a 'shallow' copy of a given dictionary- when modified, the original does not change alongside it.
languages = {1:"English",
             2:"Punjabi",
             3:"Hindi",
             4:"German",
             5: "French"}

lang_copy = languages.copy()
print(lang_copy) # Returns copy of languages dict

#3) fromkeys()- this method creates a dictionary using a given iterable as the keys. The values may be provided by the user but if not, the default is none.
k = {"a", "b", " c", "d"}
v = 10
myDict = dict.fromkeys(k,v)
print(myDict)

#4) get()- this method returns the value associated with a specified key. If they key is present in the dictionary, then the default value returned is None.
supernatural = {"name": "Dean", "species": "human","death": "season 13" }
print(supernatural.get('species')) # returns 'human'

#5) items()- this method returns a given dictionary's keys and their values (the pairs) as tuples in a list formay. This is a  view object and will reflect changes made to the original dictionary.
print(supernatural.items()) #returns the items within the supernatural dictionary

#6) keys()- this method returns a list of the keys in a given dictionary. This is also a view object and will reflect changes made to the original dictionary.
print(supernatural.keys()) #returns the keys of supernatural dict(e.g. name)

#7) pop()- this method removes an item when given a specified key and returns its value. When there is no item with this given key and no value to return is provided as a parameter, an error is raised.
snacks = {1:"ice cream",2:"sweets",3:"doughnuts",4:"chocolate",5:"yoghurt",6:"fruit"}
print(snacks.pop(3)) # returns doughnuts
print(snacks) #shows 3rd item has been removed

#8) popitem()- this method removes and returns the last key/value pair inserted in a given dictionary. A key error is raised if the dictionary is empty.
hsm = {1:"Sharpay",2:"Troy",3:"Gabriella",4:"Zeke",5:"Taylor",6:"Chad",7:"Ryan",8:"New girl"}
hsm.popitem() #returns last pair- 8: New girl
print(hsm) #shows it has been removed

#9)- setdefault()- this method returns the value associated with the specified key. Where a key does not exist, the optional value parameter allows this given value to become they key's value.
#the default value when none is provided is None.
skins = {"Tony":1, "Freddie":2, "Effy": 3}
season = skins.setdefault("Effy")
print(season)

#10) update()- this method inserts an additional given iterable object (that has key/value pairs) or another dictionary into the original dictionary.
jungle_book = {1:"Mowgli",2: "Baloo", 3: "Hathi",4: "King Louie",5:"Panther"}
print(jungle_book) #checking to compare later
updated_jungle_book = {5: "Bagheera"}
jungle_book.update(updated_jungle_book)
print(jungle_book) #shows it has been updated

#11) values()- this method returns a list of the values in a given dictionary.
jungle_values = jungle_book.values()
print(jungle_values) #return all of the values in the jungle_book dictionary