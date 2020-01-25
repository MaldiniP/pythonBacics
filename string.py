"""
A string is anything that is wrapped under a single or double quote.
"""

aNumber = "10" #wrapped under double quote
aName = 'Wangaru' #wrapped under a single quote
aDrink = 'fanta'
aNames = 'toyota'

"""
Getting a character from a string. starts with position 0
"""

theFirstLetter = aName[1]
print(theFirstLetter) # getting the position of a character is called string indexing

x = aNames[0]
print(x)
print(aNames[2])

# string slicing is getting a range of characters

newVar = 'programming'
slicedChars = newVar[-4:-8]

slicedChars = newVar[3:7]
slicedChars = newVar[3:]

print(newVar[3:7])
print(newVar[3:])
print(newVar[-4:])
print(newVar[-8:-4]) #right
print(newVar[-4:-8]) #wrong

str1 = 'Mwai'
str2 = 'Kibaki'
full_name = str1 + " " + str2 #concatenation
print(full_name)
"""
you cant edit a string _ it is immutable
"""
print(str1.lower())
print(str1.upper())