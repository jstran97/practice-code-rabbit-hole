import math

def swap(list, first_index, second_index):
  temp = list[first_index]
  list[first_index] = list[second_index]
  list[second_index] = temp

def partition(list, pivot, left, right):
  pivot_val = list[pivot]
  print(f'pivot_val: {pivot_val}')
  partition_index = left
  print(f'partition_index: {partition_index}')
  
  i = left
  while i < right:
    if list[i] < pivot_val:
      swap(list, i, partition_index)
      partition_index += 1
    i += 1

  swap(list, right, partition_index)
  print(f'partition_index: {partition_index}')
  return partition_index


def quick_sort(list, left, right):
  length = len(list)
  pivot = 0
  partition_index = 0

  if left < right:
    pivot = right
    partition_index = partition(list, pivot, left, right)

    # Sort left and right partitions
    quick_sort(list, left, partition_index - 1)
    quick_sort(list, partition_index+1, right)

  return list

list_1 = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

# Select first and last index as 2nd and 3rd arguments
answer = quick_sort(list_1, 0, len(list_1)-1)
print(answer)
