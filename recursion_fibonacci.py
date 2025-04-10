# Given a number N, return the index value of the Fibonacci sequence, where the sequence is:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
# The pattern of the sequence is that each value is the sum of the previous 2 values, which means that for N = 5 -> 2 + 3

# Time Complexity (Iterative / Loop Approach): O(n)
def fibonacci_iterative(n):
  list = [0, 1]

  index = 2

  while index < n + 1:
    # Add (sum value = 1st prev value + 2nd prev value) to list
    list.append(list[index - 1] + list[index - 2])
    index += 1

  print(list)

  return list[n]


# Time Complexity (Recursive Approach): O(2^n) (Left half of tree + Right half of tree)
def fibonacci_recursive(n):
  if n < 2:
    # if n = 0, return 0
    # if n = 1, return 0 + 1 = 1
    return n

  return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# print(fibonacci_iterative(2))
# print(fibonacci_iterative(3))
# print(fibonacci_iterative(5))
# print(fibonacci_iterative(8))

print(fibonacci_recursive(2))
print(fibonacci_recursive(3))
print(fibonacci_recursive(5))
print(fibonacci_recursive(8))


