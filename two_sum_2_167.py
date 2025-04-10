

"""
# Brute Force Approach
Compare every single number in array "numbers" to each other while trying to find which number combinations added up to the "target" number

# Downside(s) with Brute Force Approach
Time Complexity: O(n^2) (takes too long)



# Better Approach
Since array is sorted in NON-DECREASING ORDER (>= previous number), we know that: 
    SMALLER SUMS would come from the LEFT HALF of the array
    LARGER SUMS would come from the RIGHT HALF of the array

Therefore, with TWO (2) POINTERS at EACH ENDPOINT (LEFT AND RIGHT) of the array, we can choose to move EITHER POINTER to the RIGHT to INCREASE our current sum value, OR to the LEFT to DECREASE our current sum ValueError
    In other words:
        if current sum = TOO SMALL, move "l" pointer to the RIGHT -->
        if current sum = TOO LARGE, move "r" pointer to the LEFT <--

        We keep on doing this UNTIL our CURRENT SUM VALUE MATCHES the "target" sum value
"""


inputList = [1, 2, 3, 4, 5, 6, 7, 8]

def findTwoNum(numList, targetSum):

    print(len(numList))

    if len(numList) == 0:
        return None
    else:
        print(f'Input List: {numList}')
        print(f'Target Sum: {targetSum}')

        leftPointer = 0
        rightPointer = len(numList) - 1
        currentSum = numList[leftPointer] + numList[rightPointer]

        while currentSum != targetSum:
            if currentSum < targetSum:
                leftPointer += 1
            else: # If current sum > target sum
                rightPointer -= 1

            currentSum = numList[leftPointer] + numList[rightPointer]
                
        print(f'Indices found: {[leftPointer+1, rightPointer+1]}')
        return [leftPointer+1, rightPointer+1]
    
# inputList = [1, 2, 3, 4, 5, 6, 7, 8]
# print(inputList)
findTwoNum(inputList, 20)
