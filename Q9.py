# 9.	Write a function to check if the input number is prime or not



num=int(input("enter a number"))
if num==2 or num==3:
    print("{} is a prime number".format(num))
else:
    
    flag=0
    for i in range(2,num):

        if num%i==0:
            flag=1
        if flag==1:
            print("{} is not a prime number".format(num))
            break
        elif i==num//2 and flag==0:
            print("{} is  a prime number".format(num))
            break



