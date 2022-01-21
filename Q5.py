#  Given an list with N elements, task is to find the count of factors of a number X
#    which is product of all list elements.
# 	Input : 3 5 7
# 	Output : 8
# 	3 * 5 * 7 = 105, the factors of 105 are 1,
# 	3, 5, 7, 15, 21, 35, 105 whose count is 8


import math

elements=int(input("how many elements you want to enter in the list"))
l1=[]

for i in range(1,elements+1):
    l1.append(int(input("enter {}th element".format(i))))
prod=1
for i in l1:
    prod=prod*i
print(prod)
count=0
for j in range(1,prod+1):
    if prod%j==0:
        count=count+1
print(count)
    
