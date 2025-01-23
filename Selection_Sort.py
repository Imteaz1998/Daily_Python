def selection(arr):
    n=len(arr)
    
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
          if(arr[j]<arr[min]):
            min=j
        arr[i],arr[min]=arr[min],arr[i]
    
    return arr



selection_sort=[22,19,70,6,30]
result=selection(selection_sort)
print(result)