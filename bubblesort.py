def bubblesort(arr):
    n=len(arr)
    for passes in range(0,n):
        for j in range(0,n-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr



unsorted_list=[10,90,85,64,33]
sorted_list=bubblesort(unsorted_list)
print(sorted_list)