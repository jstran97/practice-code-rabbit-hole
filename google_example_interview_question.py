"""
google_example_interview.py
"""

# Given 2 arrays, create a function that let the user know (true/false) whether these two arrays contain any common items

# For example:
# l1 = [1, 2, 3, 9]
# Sum of both numbers in pair = 8
# Expected output: Not possible

# l2 = [1, 2, 4, 4]
# Sum of both numbers in pair = 8
# Expected output: Yes, possible

# What are my inputs?
# What are my outputs?
# What data type would you like the output to be in?

# Memory?
# List?
# Array?
# Ascending Order? Or is it in Descending Order or Not Sorted?
# ---- Do the elements of the array/list need to be sorted?
# Integers? Floats? Positive or negative?

# What is the most important value of the problem?
# How large will the input list/array be?
# Is time complexity (Big O, Speed) more important than space complexity (Memory)?

# Naive / Brute Force Method
l1 = [1, 2, 3, 9]
l2 = [1, 2, 4, 4]
desired_sum = 8


# O(n) - Linear Time Complexity
def hasPairWithSum(list, sum):
  # Check for empty list
  if list:
    for index in range(len(list)):
      print(index)
      next_index = index + 1
      # Check to make sure that we're not attempting to access value outside of index range
      if next_index < len(list):
        print(next_index)
        if list[index] + list[next_index] == sum:
          print('Found matching pair!')
          return True

    # Matching pair not found
    print('Matching pair not found... sadge')
    return False


findTargetSum(l1, desired_sum)

# Brute Force approach is NOT the best since it compares ADJACENT PAIRS; so it'd ultimately TRAVERSE the ENTIRE list
# It does NOT check elements at BOTH ends of the list to each other; Not inclusive

# How would you improve the code?
# Does the new method / improvement work?
# Is there another approach?
# Is this code readable?
# What would you google to improve?
# How can performance be improved?


# Improved solution (using complements (desired_sum - current val = complement val))
l1 = [1, 2, 3, 9]
l2 = [1, 2, 4, 4]
desired_sum = 8


# O(n) - Linear Time Complexity
def hasPairWithSum(list, _desiredSum):
  # Check for empty list
  if list:

    complements = []
    
    for num in list:
      if (_desiredSum - num) in complements:

        print(f'Current number/value: {num}')
        print(complements) # TESTING PURPOSES
        print('Matching pair found!')
        return True

      complements.append(_desiredSum - num)

    # Matching pair not found
    print(complements)
    print('Matching pair not found.... sadge')
    return False



hasPairWithSum(l2, desired_sum)
