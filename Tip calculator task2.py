# Subscripting
from operator import length_hint

#print("Hello"[0])

# String
#print("123" + "345")  # Concatenation

# Integer = Whole Number
#print(123 + 345)

# Large Integers
#print(123_345_678)

# Float = Floating Point Number
#print(3.12345)

# Boolean
#print(True)
#print(False)

#len("12345")

#print(type("Hello"))   # type is used to check data type

#print(type("String"))
#print(type(123))
#print(type(123.345))
#print(type(True))

#print(int("123") + int("345"))  # convert data type into others
#int()
#float()
#str()
#bool()

#print("Number of letters in your name: " + str(len(input("Enter your name")))) # this is what i did just putted str in program

# this is what she did down below
#name_of_the_user = input("Enter your name")
#length_of_name = len(name_of_the_user)

#print("Number of letters in your name: " + str(length_of_name ))
#
# print("My age: " + str(12))
# print(123 + 345)
# print(7 - 3)
# print(3 * 2)
# print(6 / 3)    # floating return
# print(6 // 3)   # integer
# print(2**3)     # POWER OF ANY NUMBER

# PEMDAS

# ()
# **
# * OR /
# # + OR _
# print(3 * 3 + 3 / 3 - 3)
#
# print(3 * (3 + 3) / 3 - 3)

# bmi = 84 / 1.65**2
# print(bmi)
#
# print(int(bmi))
#
# print(round(bmi))
#
# print(round(bmi, 2))  # rounds the 1st 2 digits of floating numbers


score = 0

# user scores a point
# score += 1
# print(score)

#
# Score = 0
# height = 1.8
# is_winning = True
#
# print(f"your score is: {score}", f"your height is: {height}", "your winning is: {is_winning}")
# # this is F string

print("Welcome to the tip calculator!")
bill = float(input("what is your total bill? $"))
tip = int(input("how much tip would you like to give? 10 15 20 "))
people = int(input("how many people to split bill with? "))
tip_percentage = tip / 100
total_bill = bill * tip_percentage
with_tip = bill + total_bill
bill_per_person = with_tip / people
final_amount = round(bill_per_person, 2)
print(f"Each person will pay {final_amount}.")
