# Write two functions that finds the factorial of any number.
# One should use Recursion, the other should use a For Loop.


def find_factorial_recursive(num):
  if num == 1 or num == 0:
    return 1
  elif num == 2:
    return 2
  # Recursion of num! = num * num - 1 * num - 2 *....
  return num * find_factorial_recursive(num - 1)


def find_factorial_iterative(num):
  answer = 1

  if num == 1 or num == 0:
    return 1
  elif num < 0:
    print("Negative integers are not allowed")
    return 0

  # Continue calculating factorial result and stop at num = 1
  while (num > 1):
    answer *= num  # answer = answer * num
    num -= 1  # num - 1

  return answer


# print("Recursive approach")
# print(find_factorial_recursive(5))
# print(find_factorial_recursive(1))
# print(find_factorial_recursive(0))

print("Iterative approach")
print(find_factorial_iterative(5))
print(find_factorial_iterative(1))
print(find_factorial_iterative(0))
print(find_factorial_iterative(-1))
