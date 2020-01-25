
"""
if 10+10 == 21:
    print("Paul")
else:
    print("name")


marks = int(input("Enter your marks:"))
if marks >= 80 and marks <=100:
    print("Grade A")
elif marks >=70 and marks <=79:
    print("Grade B")
elif marks >=60 and marks <=69:
    print("Grade C")
elif marks >=50 and marks <=59:
    print("Grade D")
elif marks >0 and marks <50:
    print("FAIl")
else:
    print("Invalid Marks")



# create and application less than 5 print too short if more than 15 too long else account successfuly logged in

password = str(input("Input your password:"))

if len(password)<5:
    print("Password is too short")
elif len(password)>15:
    print("Password is too long.")
elif len(password)>=5 and len(password)<= 15:
    print("Successfully Logged In!")
else:
    print("Invalid account")



# create an application ask for marks for mat, eng, kisw.... print report card with total, averagage, then grade


Maths = int(input("Enter Mathematics marks:"))
Eng = int(input("Enter English marks:"))
Kisw = int(input("Enter Kiswahili marks:"))
Science = int(input("Enter Science marks:"))
Social_S= int(input("Enter Social Studies marks:"))
Cre = int(input("Enter Social CRE marks:"))

total_marks = Maths+Eng+Kisw+Science+Social_S+Cre
average = total_marks/6

print("TOTAL MARKS",total_marks)
print("AVERAGE SCORE",average)

if average >= 80 and average <=100:
    print("Grade A")
elif average >=70 and average <=79:
    print("Grade B")
elif average >=60 and average <=69:
    print("Grade C")
elif average >=50 and average <=59:
    print("Grade D")
elif average >0 and average <50:
    print("FAIL")
else:
    print("Invalid Marks")
"""

"""
#username
#email
#Password

username = "WangaruP"
email_address = "wangarupaul@gmail.com"
my_password = "claSS765#."

print("WELCOME. LOG IN TO FACEBOOK")

username_d = str(input("Enter username:"))

if username_d==username:
    em = input("Enter email address:")
    if em == email_address:
        paswd = input("Enter Password:")
        if paswd == my_password:

            print("login successful!")
        else:
            print("invalid password")
    else:
        print("incorrect email address")
else:
    print("incorrect username")


#take two int values from and print greatest among them

Number_1 = int(input('Enter your first selection: '))
Number_2 = int(input('Enter your second selection: '))

if Number_1 > Number_2:
    print(f'{Number_1} is greater than {Number_2}')
else:
    print(f'{Number_2} is greater than {Number_1}')


Account_balance=500
Amount_spend=int(input("Enter the amount you want to spend: "))

if Amount_spend>Account_balance:
    print("YOUR ACCOUNT BALANCE IS INSUFFICIENT")
elif Amount_spend = 0
    print("YOUR SUCCESFULY BOUGH BALANCE IS INSUFFICIENT")



"""

t1 = 1,2,3,4,5

def f(x):
    return x[0], x[-1]
print(f(t1))
