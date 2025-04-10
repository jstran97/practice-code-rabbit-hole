import math


def merge(left, right):
  result = []
  left_index = 0
  right_index = 0

  print("Beginning of merge() function:")
  print("left: ", left, "right: ", right)

  count = 0

  # As long as there's an element in both left and right lists
  while left_index < len(left) and right_index < len(right):
    if left[left_index] < right[right_index]:
      result.append(left[left_index])
      left_index += 1
    else:
      result.append(right[right_index])
      right_index += 1

    count += 1
    print(f'Loop Iter #{count}: result = {result}')

  # Append remaining / un-added element(s) to new list based on where left off
  result.extend(left[left_index:])
  result.extend(right[right_index:])
  print(f'result (BEFORE merge() return statement): {result}')

  return result


def merge_sort(list):

  if len(list) <= 1:
    return list

  # Split list into left and right portions
  length = len(list)
  middle = math.floor(length / 2)
  left = list[0:middle]
  right = list[middle:]

  print(left)
  print(right)

  # Continue to divide list into left and right (until there's only 1 element)
  # Then start sorting and merging the sub-lists into a larger list
  return merge(merge_sort(left), merge_sort(right))


list_1 = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

answer = merge_sort(list_1)
print(answer)
