"""
in python: 1. list
              2. tupple
              3.dictonary
"""

#in python lists are mutable
my_numbers = [1,2,3,4,5,6,7,8,9]
my_floats = [1.1,2.45,3.67,40.34,5.45,60.7,72.4,8.45,9.00]
my_pets = ["cat","dog","rat","hen"]
my_bool = [True,False,True,True,False, True]
my_mixed = [1,"hello",False,10.5]
list_of_list = [[1,2,3],[10,"10",True,[9,9,False]],["new",23,10.4,False]]

#list indexing

myVar = my_numbers[6]
print(myVar)

# or

print("Get number7", my_numbers[-2])
print("Get number7", my_numbers[6])


print(my_numbers[1:5]) #indexing positive
print(my_numbers[-8:-4]) #indexing minus
print(my_numbers[::]) #indexing minus
print(my_numbers[::-1]) #indexing minus

print(my_numbers[::-1]) # reveresing


print(my_numbers[:-2])
print(my_numbers[::3])

print(my_pets[::2])
print(my_numbers[::2])

list1 = (list_of_list[1][2])
list2 = (list_of_list[1][3][2])
print(list1)
print(list2)

print(list_of_list[1][2],"and",list_of_list[1][3][2])

"""
a tuple is immutable
"""
dow = ("m","t","w","th","fr","sa","su")



