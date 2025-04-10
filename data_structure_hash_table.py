"""
google_interview.py
Find first recurring character in given array
"""


# Google Question
# Given an array = [2, 5, 1, 2, 3, 5, 1, 2, 4]
# It should return 2

# Given an array = [2, 1, 1, 2, 3, 5, 1, 2, 4]
# It should return 1

# Given an array = [2, 3, 4, 5]
# It should return undefined/None


# What are the most important points of the problem? Do you have time, space, memory, etc? What is the main goal?

# Brute Force Approach:
# O(n^2) Time Complexity
# O(1) Space Complexity (due to no extra data structure being created in memory)
def find_first_recurring_num_1(list):

  i = 0
  j = i + 1  # Increment index of inner loop as outer loop index increments to prevent starting at beginning of list each outer loop iter
  
  while i < len(list):
    while j < len(list):
      # If first (recurring) match is found
      if list[i] == list[j]:
        print('Found it!')
        return list[i]
      j += 1
      
    i += 1

  # If no recurring match is found
  return None

# Improved Solution: 
# O(n) Time complexity
# O(m) Space Complexity (due to dict {} we created in memory)
def find_first_recurring_num_2(list):
  dict = {}
  index = 0

  # As long as index is less than length of list, and list is not empty
  while index < len(list):
    # Check if num already exists in dict (access dict = O(1))
    # If it does, then return first recurring num found
    if list[index] in dict.keys():
      print(dict)
      return list[index]     # O(1)
    else:
      # Otherwise, add key-value pair to dictionary (key = list[index])
      dict[list[index]] = True  # O(1)
    
    index += 1  # O(1)

  # If no match, return None
  return None  # O(1)

print(find_first_recurring_num_2([2, 5, 1, 2, 3, 5, 1, 2, 4]))
print(find_first_recurring_num_2([2, 1, 1, 2, 3, 5, 1, 2, 4]))
print(find_first_recurring_num_2([2, 3, 4, 5]))
print(find_first_recurring_num_2([2,5,5,2,3,5,1,2,4]))


