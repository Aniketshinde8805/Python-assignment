# 4. Given a string of lowercase characters from ‘a’ – ‘z’.
#    We need to write a program to print the characters of this string in sorted order.
# 	Input : 'python'
# 	output: 'hnopty'


str1=input("enter a string in lower case")
str2=sorted(str1)
print("sorted string=","".join(str2))