def fibonacciMaster(num):
  cache = {}

  def fib(n):
    # If already calculated and stored in cache, retrieve value
    if n in cache:
      return cache[n]
    # If not in cache, calculate and store results
    else:
      if n < 2:
        return n
      else:
        cache[n] = fib(n - 1) + fib(n - 2)
        print(f'Before exiting 2nd else statement: {cache[n]}')
        return cache[n]

  return fib(num)


print(fibonacciMaster(7))
print(fibonacciMaster(8))