lst = [] 
   
n = int(input("Enter number of elements : ")) 
  

for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele)
print("original list: ")      
print(lst)
lst2=[]
for i in range(0,n):
    if lst[i]%2==0:
      lst2.append(lst[i])

print("new list:")
print(lst2)
