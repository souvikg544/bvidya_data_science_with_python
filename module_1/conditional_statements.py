# Condition to understand whether a number is odd or even

# num = int(input("Enter a number : "))
#
# if(num % 2 == 0):
#     print("Even")
# else:
#     print("Odd")

# Write a program to find the discount and the amount of a bill in a resturant :

# Bill    -    Discount
# >5000          30 %
# >2500 & < 5000  20 %
# >1000 & <2500     15 %
# <1000             5%
#

bill = int(input("Enter your bill amount : "))
discount=0.0


if(bill >= 5000):
    discount=(30/100)*bill
elif((bill >=2500) & (bill < 5000)):
    discount=0.2* bill
elif((bill>=1000)&(bill<2500)):
    discount=0.15 * bill
else:
    discount= 0.05 * bill

print("Your Discount is : Rs",discount)

amount= bill - discount

print("Your amount is : Rs",amount)




