
# 6. Given a list, find the difference between highest occurrence and least occurrence of any number in a list
# 	Examples:
# 	Input : [7, 8, 4, 2, 4, 4, 1, 1, 7, 7, 2, 5]
# 	Lowest occurring element (5) occurs once.
# 	Highest occurring element (7) occurs 3 times
# 	In case of tie take lower number

l1=[7, 8, 4, 2, 4, 4, 1, 1, 7, 7, 2, 5]
l2=list(set(l1))
l3=[]
for i in l2:
    l3.append(l1.count(i))
print(l3)
maxvalue=max(l3)
minvalue=min(l3)
print(maxvalue - minvalue)
