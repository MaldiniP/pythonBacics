# Task 1
# Write a Python program to calculate the length of a string.

in_string = "programming"
length_of_string = len(in_string)
print(length_of_string)


# Task 2
# Write a Python program to count the number of characters (character frequency) in a string.
# hint use the inbuilt funtion Counter

string_name = "statements"
from collections import Counter

res = Counter(string_name)
print(res)

# Task 3
# Write a Python program to count the occurrences of the word "python" in a given sentence below:
# "We are learning how to program in python. I find python programming fun"

sentence = "We are learning how to program in python. I find python programming fun"
occ = sentence.count("python")

print(occ)

# Task 5
# Write a Python function to reverses the word below:
# reven

my_word = "reven"
rev_word = my_word[::-1]

print(rev_word)


# Task 6
# task_list = [23, “Jane”, [“Lesson 23”, 560, {“currency” : “KES”}], 987, (76,”John”)]
# Determing type of variable in taskList using an inbuilt function

task_list = [23, "Jane", ["Lesson 23", 560, {"currency" : "KES"}], 987, (76,"John")]
print(task_list)

type_task_list = type(task_list)
print(type_task_list)

# Task 7
# Print KES

print(task_list[2][2]["currency"])

# Task 8
# Print 560

print(task_list[2][1])

# Task 9
# Use a function to determine the length of task_list

length = len(task_list)
print(length)

# Task 10
# Change 987 to 789 without using an inbuilt - method or Assignment

x = task_list[3]
y = str(x)
z = y[::-1]
a = int(z)

task_list[3] = a
print(task_list)

# or

task_list[3] = 789
print(task_list)

# Task 11
# Change the name “John” to “Jane” .
# impossible tupples are immutable

#or

task_list[4] = (76, 'Jane')
print(task_list)


"""
first_number = int(input('Enter first number: '))
second_number = int(input('Enter second number: '))

if first_number > second_number:
    print(f'{first_number} is greater than {second_number}')
else:
    print(f'{second_number} is greater than {first_number}')
    """


a = ['foo', 'bar', 'baz', 'qux']
s = 'corge'

i = 0
while i < len(a):
    if a[i] == s:# Processing for item found
        break
        i += 1
    else: # Processing for item not found
print(s, 'not found in list.')

corge not found in list.



