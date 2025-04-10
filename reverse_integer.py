"""
NeetCode

You are given a signed 32-bit integer x.

Return x after reversing each of its digits. After reversing, if x goes outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0 instead.

Solve the problem without using integers that are outside the signed 32-bit integer range.
"""



# Time Complexity: O(n)
# Space Complexity: O(1)
def reverse_integer(num: int) -> int:
    # if num < 0:

    num_string = str(num)
    print(num_string)

    result = ''
    index = len(num_string) - 1

    if num < 0:
        # Start with negative sign (-)
        result = num_string[0]

        while index >= 1:
            # Append char of string to new string in reverse order
            result = result + num_string[index]
            index -= 1

    else:
        while index >= 0:
            # Append char of string to new string in reverse order
            result = result + num_string[index]
            index -= 1

        # Alternative method:
        #reversed_string = num_string[::-1]

    print(result)

    if not -0x7FFFFFFF < int(result) < 0x7FFFFFFF:
        return 0
    else:
        return int(result)



num = -1234
reverse_integer(num)