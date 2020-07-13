def partition(arr,low,high):
  i = (low - 1)
  pivot = arr[high]

  for j in range(low,high):
    if arr[j] <= pivot:
      i += 1
      #Swap the position of the value less than the pivot with the next value bigger than the pivot
      arr[i],arr[j] = arr[j], arr[i]
    print(arr)
  #Put the partition in the correct index. Everything before the partition index will be less than the partition and everything after will be greater than the partition
  arr[i+1],arr[high] = arr[high],arr[i+1]
  #return partition index
  return i + 1

def quickSort(arr,low,high):
  if low < high:
    partitionIndex = partition(arr,low,high)
    #Sort elements before partition
    quickSort(arr,0,partitionIndex-1)
    #Sort elements after partition
    quickSort(arr,partitionIndex+1,high)
  return arr

arr = [10, 7, 8, 9, 3,2, 1, 5] 
lenArr = len(arr)
print(quickSort(arr,0,lenArr-1))