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

taskList = [23,"Jane",["Lesson23",560,{"currency" : "KES"}],987,(76,"John")]
print(taskList)
print(taskList[1])
print(taskList[2][2]['currency'])
print(taskList[2][1])


taskListLength = len(taskList)
print(taskListLength)

myNumberx = taskList[3]
print(myNumberx)

myDictionary = {"Product" : "Lifevest"}
print(type(myDictionary))

#syntax

this_dict ={
    "name":"Paul",
    "interest":["swimming", "football"],
    "age":16,
    "workday":("mon", "tue", "wed"),
    "parents":{
        "mother":{
            "first_name":"sarah"
        }
    }
}

print(this_dict)

print(this_dict["parents"]["mother"]["first_name"])


# my dictionary

"""
my_dictry = {
    "my_name":"Paul",
    "primary_schools":
        {
        "first_p":"Ronald Ngala",
            {
            "approximate_pop":
                {"boys" : 500,
                 "girls": 650,
                 "total":100
                 },
            },
            {
            "headteacher":
                {"first_name":""James"},
                {"second_name":""Muhoti"},
            }
        },
        {"second_p":"James Gichuru",
            {
            "approximate_pop":
                {"boys" : 100, "girls": 200, "total":300},
            },
            {
            "headteacher":"Otieno"
            }
        }
        }
}
}
"""

# task 3
numbers = [1023, 43546, 678345, 54767]
print(max(numbers))
print(numbers[1])

new_listw =[]
new_listw.append(numbers[0])
new_listw.append(numbers[-1])

print(new_listw)


tuppleOne = (1,2,3,4,5,6,7,8,9,10)

print(tuppleOne)
first_half = tuppleOne[0:5]
second_half = tuppleOne[5:]
print(first_half)
print(second_half)

B1= str(first_half)
print(type(B1.strip("()")))
B2= str(second_half)

print(B1.strip("()"))
print(B2.strip("()"))




