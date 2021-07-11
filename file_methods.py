# Section 7: Python file methods- describe each method and provide an example
#the original file contents are pasted at the bottom of this document :)

# File Methods
#1) read()- this method returns the bytes that are read from the file in a string.
# There is an optional size parameter which allows you to specify the number of bytes- the default is -1 which means the whole file will be read.
f = open("karan_info.txt", "r")
print(f.read()) # returns text in the karan_info.txt file.

#2) readline()- this method returns a singular line from a file. The optional size parameter allows you to specify the number of bytes to be read.
f = open("karan_info.txt", "r")
print(f.readline()) #returns first line of text from the txt file.

#3) readlines()- this method returns a list, in which each item of the list is a line in the file.
# The hint parameter allows you to limit the number of lines being returned by ensuring the number of bytes does not exceed the hint number given.
f = open("karan_info.txt", "r")
print(f.readlines())

#4) write()- this method allows you to write a string to a file.
# If 'a' (append) is specified when opening the file, the string will be inserted at the end of the file.
# If 'w' (write) is specified when the opening the file, the existing contents will be overwritten.
f = open("karan_info.txt", "a")
f.write("\nI think I'll eat after completing this section")
f.close()
f = open("karan_info.txt", 'r') #checking the file again
print(f.read())

#5) writelines()- this method allows you to write list items to a file.
# Similarly to write(), the position of this addition will depend on whether the file was opened to append or to writef = open("karan_info.txt", "a")
f = open("karan_info.txt", "a")
f.writelines(["\nI'm very excited to eat,", " Glad this is the last question."])
f.close()
f = open("karan_info.txt", 'r') #checking the file again
print(f.read())


####original text file
#Hi, my name's Karan.
#I'm not quite sure what to write, I just needed this text file for the assessment.
#Hmmm...
#I am quite hungry. Can't think beyond that.