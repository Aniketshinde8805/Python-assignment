
# 3. Integers X and K are given. The task is to find smallest K-digit number divisible by X.
#    (Hint - Use min function)
# 	Input : X = 83, K = 5
# 	Output : 10043 is the smallest 5 digit number that is divisible by 83.

x=int(input("enter the value of x"))
y=int(input("enter the value of y"))
min=pow(10,y-1)
max=pow(10,y)
for i in range(min,max):
    if i%x==0:
        print("minimum {} digit number divisible by {} is {}".format(y,x,i))
        break
    
