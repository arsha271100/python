str=input("enter the string")
r=str[0]
str=str.replace(r,"$")
str=r+str[1:]
print("the string is",str)