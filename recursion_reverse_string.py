# Implement a function that reverses a string using iteration (loops), and then recursion


def reverse_string_iterative(input_str):
  result = ''
  index = len(input_str) - 1
  print(index)

  while index >= 0:
    # Append char of input string to new string in reverse order
    result = result + input_str[index]
    index -= 1

  return result


def reverse_string_recursive(input_str):
  # If string is empty or has only one character
  if len(input_str) < 2:
    return input_str
  else:
    print(input_str)
    return reverse_string_recursive(input_str[1:]) + input_str[0]


if __name__ == "__main__":
  # print(reverse_string_iterative("hello"))

  print(reverse_string_recursive("hello"))
