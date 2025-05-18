"""
Input:
    Integer array "nums"

Output:
    Array rotated to the right by k steps, where k is non-negative (either positive or 0)

Restriction(s):
    k = non-negative (either positive or 0)
"""

inputArray = [1, 2, 3, 4, 5, 6, 7]
print(f'Input List: {inputArray}') # String Formatting with Placeholders and Modifiers

def rotateArrayToRight(nums, k):
    numElements = len(nums)
    k %= numElements
    
    print(k)

    # Reverse entire array
    nums.reverse()

    # Reverse the first k elements
    nums[:k] = reversed(nums[:k])
    print(nums[:k])

    # Reverse the remaining (numElements - k) elements
    nums[k:] = reversed(nums[k:])
    print(nums[k:])

    print(nums)



rotateArrayToRight(inputArray, 3)
