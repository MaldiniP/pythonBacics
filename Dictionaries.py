# task

# determine type of variable in tasklist using an inbuild function
taskList = [23,"Jane",["Lesson 23", 560, {"currency":"KES"}], 987, (76,"John")]

result1 = type(taskList)
print(result1)


# print KES

print(taskList[2][2]["currency"])

# print 560

print(taskList[2][1])

# use a function to determine the length of taskList

print(len(taskList))

# change 987 to 789

"""
taskList[3] = 789
print(taskList)
"""
# or

x = taskList[3]
y = str(x)
z = y[::-1]
a = int(z)
taskList[3] = a
print(taskList)


# change the name "john" to "jane

tupple_x = taskList[4]
string_x = str(tupple_x)
print(string_x)

result_x = string_x.strip("()")
print(result_x)
print(result_x[5:9])