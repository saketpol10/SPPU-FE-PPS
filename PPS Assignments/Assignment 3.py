n=int(input("Enter no of elements: "))
nos_list=[]                            # nos_list list is created
for i in range(n):                     # for loop
    num=int(input("Enter no: "))
    nos_list.append(num)               # numbers are added in nos_list list
maxNo=max(nos_list)                    # maximum number in list
minNo=min(nos_list)                    # minimum number in list
sumNos=sum(nos_list)                   # sum of numbers in list

average=sumNos/len(nos_list)           # average of numbers in list
print("Max no is ",maxNo)
print('Min no is ',minNo)

print('Sum of nos is ',sumNos)
print('Average of nos is ',average)