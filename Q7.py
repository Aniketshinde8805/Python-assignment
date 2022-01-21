# 7. We are given a 2D list of order N X M and a column number K ( 1<=K<=m).
#    Our task is to sort the 2D list according to values in the Column K.
#     Examples:
# 	Input : If our 2D list is given as (Order 4X4) 
# 		39 27 11 42 
# 		10 93 91 90 
# 		54 78 56 89 
# 		24 64 20 65
# 	Sorting it by values in column 3 
# 	Output :    
# 		39 27 11 42 
# 		24 64 20 65 
# 		54 78 56 89 
# 		10 93 91 90

row=int(input("enter no of rows"))
col=int(input("enter no of columns"))
l1=[]

for i in range(1,row+1):
    l2=[]
    for j in range(1,col+1):
        l2.append(int(input("enter the element{} of row{}  ".format(j,i))))
    l1.append(l2)
print(l1)

l3=[]
k=int(input("enter which column you want to sort"))
k=k-1
print("k= ",k)

for i in range(0,row):
    l3.append(l1[i][k])

print(l3)
l3.sort()
print(l3)

for i in range(0,row):
    l1[i][k]=l3[i]
print(l1)