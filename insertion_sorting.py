def insertion_sort(arr):
    for i in range(1,len(arr)): 
        for j in range(i,0,-1):
            if arr[j]<arr[j-1]:
                arr[j],arr[j-1]=arr[j-1],arr[j]
    print(arr)


insertion_sort([12, 25, 64, 22])
insertion_sort([5, 3, 1, 4, 2])