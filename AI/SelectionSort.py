def Selection_sort(array,size):
    for step in range(size):
        min_idx=step
        for i in range(step+1,size):
            if array[i]<array[min_idx]:
                min_idx=i
        (array[step],array[min_idx])=(array[min_idx],array[step]) # the minimum get swap with the current

data=[1,2,32,3,4,56]
size=len(data)
Selection_sort(data,size)
print("Selection Sort:")
print(data)