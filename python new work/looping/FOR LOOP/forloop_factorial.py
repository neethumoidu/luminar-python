#factorial using for loop
num=int(input("enter number="))
fact=1
if num>=1:
    for i in range(1,num+1):
        fact=fact*i
print(fact)