# 1. Given a number n, find the product of all factors of n.
# 	Input : 20
# 	Output : 1*2*4*5*10 = 400

num=int(input("Enter a number"))
l1=[]
for i in range(1,num):
    if num%i==0:
        l1.append(i)
print(l1)
prod=1
for j in l1:
    prod=prod*j
print(prod)