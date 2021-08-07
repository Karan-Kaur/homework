#Section 6: Python set methods- describe each method and provide an example
#1) add()- this method adds an additional item/element to the set provided it is not already in the set.
lang = {"English", "Punjabi", "Hindi", "French", "Spanish"}
lang.add("tagalog")
print(lang)

#2) clear()- this method removes all the items of a set.
alphabet = {"a", "b", "c", "d", "e"}
alphabet.clear()
print(alphabet)

#3) copy()- this method returns a duplicate copy of a given set.
movies = {"clueless", "10 things I hate about you", "27 dresses"}
movies2 = movies.copy()
print(movies2)

#4) difference()- this method checks for differences between two sets. It returns a set containing the items that exist only in the first set and not in the other
chick_flicks = {"Runaway bride", "Clueless" ,"Love actually" , "Bride Wars", "She's all that"}
fave_flicks = {"Clueless", "27 dresses", "10 things I hate about you", "Bride Wars"}
diff = chick_flicks.difference(fave_flicks)
print(diff)

#5) intersection()- this method returns a set containing items that are commonly present in the two or more given sets.
numbers = {1, 2, 3, 4, 5, 6, 7, 8}
numbers2 = {9, 7, 13, 11, 4, 18, 5}
numbers3 = {4, 8, 5, 7, 20}

overlap = numbers.intersection(numbers2, numbers3)
print(overlap)

#6) issubset()- this method checks if the items in the original set contain the items in the specified set. It returns True if this is the case and False if not.
bollywood = {"K3G", "KHNH", "KKHH"}
bollywood2 = {"KKHH", "JWM", "K3G", "KHNH", "DDLJ"}
result = bollywood.issubset(bollywood2)
print(result) #returns True

#7) issuperset()- this method checks if the items in the specified set exist in the original set- it returns True if this is the case and false if not.
AHS_seasons = {"Hotel","Freakshow", "Coven", "Asylum", "Cult", "1984", "Murder House"}
AHS2 = {"Murder House", "Asylum", "Freakshow"}
result2 = AHS_seasons.issuperset(AHS2)
print(result2) #returns True

#8) pop()- this method removes and returns a random item from a given set.
wii_games = {"Mario Kart", "Brain Academy","Wii Sports", "Wii fit"}
wii_games.pop()
print(wii_games)

#9) remove()- this method removes a specified item from a list so long as it exists- if not, an error will be raised.
TVD = {"Damon","Stefan","Elena","Caroline","Bonnie","Enzo","Alaric"}
TVD.remove("Alaric")
print(TVD)

#10) symmetric_difference()- this method returns a set containing items from the sets given that do not overlap (i.e. the items that exist in both sets will not be in the output)
num1 = {3, 12, 9, 67}
num2 = {6, 91, 12, 9, 2}
print(num1.symmetric_difference(num2))

#11) union()- this method joins two or more sets or iterable objects. It returns a set containing the items from the original set and those from the given set or iterable, provided the item is not already present in the original.
pizza = {"pepperoni", "margherita", "vegetarian"}
sides = {"fries", "chicken dippers", "garlic bread"}
united = pizza.union(sides)
print(united)

#12) update()- this method updates a set through adding the items of another set or iterable. Duplicates will not show up if items appear in both the original and additional set/iterable.
Villains = {"Scar","Ursula","Evil Queen"}
print(Villains)
Villains2 = {"Frollo","Mother Gothel"}
update_Villains = Villains.update(Villains2)
print(Villains) #comparisons show has been updated to include the extra items
