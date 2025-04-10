list_1 = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def insertion_sort(list):

  if len(list) == 0:
    return None
  else:
    # Sort by finding smaller numbers and inserting them at locations where num > left and < right
    # (Ascending order)
    for i in range(len(list)):

      # Move number to first position, and shift everything to right
      if list[i] < list[0]:
        list.insert(
          0, list.pop(i))  # Remove num from current index to first index
      else:
        # Find where next lowest number should go
        for j in range(1, len(list)):
          # If num > left number and num < right number
          if list[i] > list[j - 1] and list[i] < list[j]:
            # Insert number in between the left and right numbers
            list.insert(j, list.pop(i))

    return list


print(insertion_sort(list_1))
