def mergeSort(array):
  if (len(array) == 1):
    return array
  
  halfLen = int(len(array)/2)
  left = array[0:halfLen]
  right = array[halfLen: len(array)]
 
  return merge(
    mergeSort(left),
    mergeSort(right)
    )

def merge(left,right):
  result = []
  leftIndex = 0
  rightIndex = 0

  while(leftIndex < len(left) and rightIndex < len(right)):
    if(left[leftIndex] < right[rightIndex]):
      result.append(left[leftIndex])
      leftIndex += 1
    else:
      result.append(right[rightIndex])
      rightIndex += 1

  result = result + left[leftIndex:] + right[rightIndex:]

  return result


print(mergeSort([9,10, -9, 10231,55,1,4,0,90,8]))