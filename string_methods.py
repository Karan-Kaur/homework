# Section 2: Python string methods- describe each method and provide an example
#Note- original strings are not modified by these methods.

# 1) capitalize()- this method returns a string in which the first letter is uppercase and the following are lowercase.
capital = "hi, this is my example"
capital2 = capital.capitalize()
print(capital2) #prints 'Hi, this is my example'

# 2) casefold()- this method returns a string where all the letters are lowercase. This is considered a more 'aggressive' method compared to lower() as it works upon other languages, unicode texts etc.
fold = "HI, THIS IS MY EXAMPLE!"
fold2 = fold.casefold()
print(fold2) #prints 'hi, this is my example'

# 3) center()- this method returns a string which is centre aligned. It takes in a length parameter which determines the length of the string and an optional character parameter which takes up the space aside the centre.
toystory = "the claw"
alien = toystory.center(16, "o")
print(alien)

# 4) count()- this method counts the number of times a specified value appears in a string. The user can provide a criteria for the positions they wish to search.
sentence = "Some days I think I understand, other days I realise I do not understand"
sentence2 = sentence.count("understand")
print(sentence2) #returns 2

# 5) endswith()- this method checks a string ends with a given value and returns True if this criteria is met.
checkend = "When does this speech end?"
checkend2 = checkend.endswith("end?")
print(checkend2)

# 6) find()- this method finds the first occurence of a given value in a string and returns its position. If it does not appear, the output will be -1. There are optional position parameters which directs the method to search within a particular section.
search = "Where am I?"
search2 = search.find("a")
print(search2) #returns 6

# 7) format()- this method replaces the placeholders in the string, as defined by curly brackets ({}), with given values. The placeholders may be empty or contain variable names. The formatted string is returned.
name = 'Karan'
stream = 'software'
formatted = "My name is {} and I'm on the {} stream".format(name,stream)
print(formatted)

# 8) index()- this method finds the first appearance of a given value and returns it's position within a string. This method also has optional positional arguments
seek = "Where am I?"
seek2 = seek.index("h")
print(seek2) # returns 1

# 9) isalnum()- this method checks if a string only contains alphanumeric values. It returns true if this criteria is met.
look = "Am I alphanumeric?"
look2 = look.isalnum()
print(look2) #false since there are spaces.

# 10) isalpha()- this method checks if a string only contains letters of the alpahbet and returns True if this is the case.
letters = "Codefirstgirls"
letters2 = letters.isalpha()
print(letters2) #returns True

# 11) isdigit()- this method checks whether all the characters within a string are digits and returns True if this is the case. 0-9, subscript, superscript and decimal characters considered digits.
digits = "1234"
digits2 = digits.isdigit()
print(digits2) #returns True

# 12) islower()- this method checks whether the alphabet characters within a string are all lowercase and returns True if this is the case.
lower = "am i all lowercase?"
lower2 = lower.islower()
print(lower2) #returns True

# 13) isnumeric()- this method checks whether all the characters within a string are numeric and returns True if this is the case.
#Unicode considers the following to be numeric: integers, subscript, superscript, fractions, and roman numerals.
num = "12457"
num2 = num.isnumeric()
print(num2) #returns True

# 14) isspace()- this method checks whether the string contains just whitespaces. If so, it will return True.
blank = "  "
blank2 = blank.isspace()
print(blank2) #returns True

# 15) istitle()- this method checks whether each word in a string begins with a uppercase letter followed by lowercase letters. If the code meets this criteria, it will return True
series = "Alice In Borderland"
series2 = series.istitle()
print(series2) # returns True

# 16) isupper()- this method checks whether every letter is uppercase and returns True if this is the case.
film = "THIS IS SPARTA!"
film2 = film.isupper()
print(film2)

# 17) join()- this method joins the elemets of a given iterable object by a string separator and returns a concatenated string.
sep = '-'
nums = ('1', '2', '3', '4')
print(sep.join(nums))

# 18) lower()- this method returns a string in which all the letters in the new string are lowercase.
film = "THIS IS SPARTA"
film3 = film.lower()
print(film3)

# 19) lstrip()- this method removes characters before the string (left-hand side)- by default, white/blank space is removed but there is an optional parameter for specific characters (e.g. ".,")
strip = "     white space"
strip2 = strip.lstrip()
print(strip2)

# 20) replace()- this method returns a string that replaces a specified substring with another newly specified one.
nano = "I am on the data stream"
nano2 = nano.replace("data", "software")
print(nano2)

# 21) rsplit()- this method splits a string and returns a list object. This may be on the basis of a specified separator (e.g. ',') and a maxsplit can be defined, determining the number of splits that can be performed. In an rsplit, these splits will begin from the right.
#if no maxsplit is specified, all occurences will be considered (-1)
hello = "hi,sat sri akaal,bonjour,hola"
print(hello.rsplit(',',))

# 22) rstrip()- this method removes characters at the end of a string (right-hand side). The default is removing white/blank spaces but characters can also be specified.
strip1 = "white space   "
strip3 = strip1.rstrip()
print(strip3)

# 23) split()- this method splits a string and returns a list object- an optional separator and maxsplit may be given. This differs from a rsplit in that the splitting does not begin from the right when a maxsplit is specified.
splitting = "hi#I am Karan#I am on the software stream"
splitting2 = splitting.split("#")
print(splitting2)

# 24) splitlines()- this method splits a string at the line breaks and returns a list. The line break can be kept in through the optional parameter, which accepts True or False.
convo = 'Hello \nAre you also confused?'
print(convo.splitlines())

# 25) startswith()- this method checks whether a string begins with a specified phrase/value and returns True if they match.
start = "Do I start with a greeting?"
start = start.startswith("Do")
print(start) #returns True

# 26) strip()- this method removes characters from both the beginning and end of a string. By default, this is blank space but characters can be specified.
splitall = "     white space     "
splitall2 = splitall.strip()
print(splitall2)

# 27) swapcase()- this method returns a string in which the lowercase letters become uppercase and vice versa.
swap = "tHE hAUNTING OF hILL hOUSE"
swap2 = swap.swapcase()
print(swap2)

# 28) title()- this method returns a string in which the first letter of each word is capitalised while the following are lowercase.
title = "how to get away with murder"
title2 = title.title()
print(title2)

# 29) upper()- this method returns a string in which each letter is converted to uppercase.
#title = "how to get away with murder"
shout = title.upper()
print(shout)
