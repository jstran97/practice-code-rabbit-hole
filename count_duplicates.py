# Count # of each entry
def countDuplicateV2(nums):
    if len(nums) == 0:
        return False

    cache = {}

    # For each number, add it to the cache if it's NOT present in the array
    for num in nums:
        if num in cache:
            cache[num] += 1
        else:
            cache[num] = 1

    print(f'Cache Contents: {cache}')

    return True

arr = [1, 1, 2, 3, 4, 5, 5, 6, 5, 5, 6, 7, 8, 9, 10]
print(arr)
countDuplicateV2(arr)