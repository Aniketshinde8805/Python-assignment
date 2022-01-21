# 10. Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# 	If the given string is already ends with 'ing' then add 'ly' instead.
# 	If the string length of the given string is less than 3, leave it unchanged 

str1=input("enter a string")

if len(str1)<3:
    print(str1)
else:
    if str1.endswith('ing',-3):
        str1=str1.replace("ing","ly")
        print(str1)

    else:
        s1=str1[-3:]
        str1=str1.replace(s1,"ing")
        print(str1)