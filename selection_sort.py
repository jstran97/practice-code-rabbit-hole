def selection_sort(list):

  if len(list) == 0:
    return None
  else:
    # Sort by bringing smaller numbers to beginning of list
    # (Ascending order)
    for i in range(len(list)):

      min = i  # Set current index as minimum
      temp = list[i]

      # Find larger value of the two adjacent numbers in list
      # and move it to end of the list
      for j in range(i + 1, len(list)):
        # If current is smaller than current smallest number, update min index
        if list[j] < list[min]:
          min = j

      # Swap positions of current index and smallest number found
      list[i] = list[min]
      list[min] = temp

    return list


list_1 = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(selection_sort(list_1))
