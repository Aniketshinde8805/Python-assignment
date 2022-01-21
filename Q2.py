# 2. Integers X and K are given. The task is to find largest K-digit number divisible by X.
#     (Hint - Use max function)
# 	Input : X = 83, K = 5
# 	Output : 99932 is the largest 5 digit number that is divisible by 83.


x=int(input("enter the value of x"))
y=int(input("enter the value of y"))
min=pow(10,y-1)
max=pow(10,y)
for i in   reversed(range(min,max)):
    if i%x==0:
        print("largest {} digit no divisible by {} is {}".format(y,x,i))
        break
    