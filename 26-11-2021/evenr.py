list=[100, 2, 3, 5]
e=[]
o=[]
for num in list:
    if num % 2 == 0:
        e.append(num)
    else:
        o.append(num)
print(o)
