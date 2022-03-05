
n = int(input("Enter number of elements : "))
print("enter the values")
lst=[]
for i in range(0,n):
      ele=int(input())
      if ele > 100:
          lst.append('over')
      else:
        lst.append(ele)
print(lst)



