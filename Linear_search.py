def linear_search(arr,target):
    size=len(arr)
    for i in range(0,size):
        if(arr[i]==target):
            return i
    return -1


my_list=[10,76,80,99,55]
target=80
result=linear_search(my_list,target)
print(result)