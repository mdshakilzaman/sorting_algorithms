from random import randint

# bubble sort is all about comparing each other. O(n2)
def bubble_sort(array):
  n = len(array)
  for i in range(n):
    sorted = True
    for j in range(n - 1 - i):
      if array[j + 1] < array[j]:
        array[j], array[j+1] = array[j+1], array[j]
        sorted = False
    if sorted == True:
      break
  return array

# insertion sort is based on plaing an item to its correct position. O(n2)
def insertion_sort(array):
  for i in range(1, len(array)):
    key_item = array[i]
    j = i - 1
    while j >= 0 and array[j] > key_item:
      array[j + 1] = array[j]
      j -= 1
    array[j + 1] = key_item
  return array


# merge sort is based on merging two array(sorted) to one. O(nlogn)
def merge(left, right):
  if len(left) == 0:
    return right
  if len(right) == 0:
    return left
  result = []
  left_index, right_index = 0, 0
  while len(result) < len(left) + len(right):
    if left[left_index] <= right[right_index]:
      result.append(left[left_index])
      left_index += 1
    else:
      result.append(right[right_index])
      right_index += 1
    if left_index == len(left):
      result += right[right_index:]
      break
    if right_index == len(right):
      result += left[left_index:]
      break
  return result

def merge_sort(array):
  if len(array) < 2:
    return array
  mid = len(array) // 2
  left = array[:mid]
  right = array[mid:]
  return merge(merge_sort(left), merge_sort(right))


#quicsort algorithm which is based on selecting a pivot element. O(nlogn)
def quick_sort(array):
  if len(array) < 2:
    return array
  low, same, high = [], [], []
  pivot = array[randint(0, len(array) - 1)]
  for item in array:
    if item < pivot:
      low.append(item)
    elif item > pivot:
      high.append(item)
    else:
      same.append(item)
  return quick_sort(low) + same + quick_sort(high)
  

  
array_length = 10
x = [randint(0, 1000) for i in range(array_length)]
print("unsorted array", x)
y = bubble_sort(x)
print(y)

y = insertion_sort(x)
print(y)

y = merge_sort(x)
print(y)

y = quick_sort(x)
print(y)