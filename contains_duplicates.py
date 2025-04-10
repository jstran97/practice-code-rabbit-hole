# Return True if any value appears more than once in the array. Otherwise, return False
def hasDuplicate(nums):
    if len(nums) == 0:
        return False

    seen = set()

    # For each number, add it to the set (unique numbers only) if it's NOT present in the array
    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False