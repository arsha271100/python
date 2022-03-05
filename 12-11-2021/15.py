a = int(input("enter the value of a"))
b = int(input("enter the value of b"))
op = int(input("enter the operator click 1.+ 2.* 3./ 4.-"))
if op == 1:
  c = a+b
  print(c)
elif op == 2:
  c = a*b
  print(c)
elif op == 3:
  c = a/b
  print(c)
elif op == 4 and a > b:
  print("value",a-b)
elif a < b:
  print("value",b-a)
else:
  print("invalid")


