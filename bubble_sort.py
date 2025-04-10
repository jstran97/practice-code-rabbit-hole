def bubble_sort(list):

  if len(list) == 0:
    return None
  else:
    # Sort by propagating larger numbers to end of the list
    for i in range(len(list)):
      # Find larger value of the two adjacent numbers in list
      # and move it to end of the list
      for j in range(len(list)):
        # Swap positions of left number and right number in list if right > left
        if list[j] > list[i]:
          temp = list[j]  # Temp variable
          list[j] = list[i]
          list[i] = temp

    return list


list_1 = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(bubble_sort(list_1))
