import time


class MyArray:
  # Constructor to initialize object
  def __init__(self, length=0, list=[]):
    # Attributes
    self.length = length
    self.data = list

  def getValue(self, index):
    return self.data[index]

  def append(self, value):
    print(self.length)

    # self.data[self.length - 1] = value
    # self.length += 1


def reverse_string1(str):
  """Reverse the given string"""
  # Check if string is given and if string is greater than 1 character
  if str and len(str) > 2:
    return str[::-1]


def mergeSortedArrays(arr1, arr2):
  """Merge the two given arrays into one, and then sort it"""
  if arr1 and arr2:
    # Store array 1 contents in new array (merged_arr)
    merged_arr = arr1
    print(merged_arr)

    # Append array 2 contents to end of new array (merged_arr)
    merged_arr.extend(arr2)

    # Sort all array contents in ascending order (lowest to highest #)
    merged_arr.sort()
    print(merged_arr)
    return merged_arr


arr = MyArray()
# arr.append(1)
# print(arr.getValue(0))

str_1 = 'Hi my name is Andrei'
print(str_1)

# Start timer
tic = time.perf_counter()

rev_str = reverse_string1(str_1)
print(rev_str)

# Stop timer
toc = time.perf_counter()
print(f"Ran reverse_string1() in {toc-tic:0.8f} seconds")

given_arr1 = [0, 3, 4, 31]
given_arr2 = [4, 6, 30]
given_arr3 = []
# Start timer
tic = time.perf_counter()

merged = mergeSortedArrays(given_arr1, given_arr2)

# Stop timer
toc = time.perf_counter()
print(f"Ran mergeSortedArrays() in {toc-tic:0.8f} seconds")
