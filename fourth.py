#name="python"
#for i in name:
   # print(i)
#nested loop
list1 = []
even  = []
for i in range(1,101):
    list1.append(i)
for i in list1:
    if(i%2==0):
        even.append(i)
print(even)


