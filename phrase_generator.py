# You are given a string of available characters and a string representing a word or a phrase that you need to generate.
# Write a function that checks if you cab generate required word/phrase using the characters provided.
# If you can, then please return True, otherwise return False.
# 
# NOTES:
#     You can only generate the phrase if the frequency of unique characters in the characters string is equal or greater
#     than frequency in the document string.

# IMPORTANT:
#     The phrase you need to create can contain any characters including special characters, capital letter, numbers
#     and spaces.
# 
#     You can always generate an empty string.


from collections import Counter

def generate_phrase(characters, phrase):
    if len(characters) < len(phrase): #ensuring there are enough characters
        print('Not enough characters to generate phrase')
        exit()
    else:
        charcount = Counter(characters) #count of each unique character
        # print(charcount)
        phrasecount = Counter(phrase)
        # print(phrasecount)
        overlapcounts = charcount & phrasecount #output is the common values
        if overlapcounts == phrasecount:
            # print(overlapcounts)
            return True
        else:
            return False

#experimenting
print(generate_phrase('ktarrttagn', 'karan'))
print(generate_phrase('katrn', 'karan'))
print(generate_phrase('ktarrttang?', 'karan?'))
print(generate_phrase('', ''))
print(generate_phrase('wor jinkjwg?_feomr', ' work_'))
print(generate_phrase('worjinkjwg?_feomr', ' work_'))
print(generate_phrase('wor', ' work'))
