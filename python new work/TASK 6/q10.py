# 10. Write the program to find the lists consist of at least one common element. 
l1=[10,11,20,30,32]
l2=[15,16,20,30,31]
result=[]
for element in l1:
    if element in l2:
        result.append(element)
print("common element in the list 1 and list 2 are :-",result)