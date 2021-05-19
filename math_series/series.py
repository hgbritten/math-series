# https://www.programiz.com/python-programming/examples/fibonacci-recursion


def fibonacci(n):

  if n <= 1:
    return n
  else:
    return(fibonacci(n-1) + fibonacci(n-2))


# https://www.codespeedy.com/print-nth-iteration-of-lucas-sequence-in-python/

def lucas(n):
  if n == 0:
    return 2
  if n == 1:
    return 1
  return lucas(n-1) + lucas(n-2)

def sum_series(n, i = 0, j = 1 ):
  if n == 0:
    return i
  if n == 1:
    return j
  return sum_series(n-1,i,j) + sum_series(n-2,i,j)
  # if i == 2:
  #   return sum-series(i-1) + sum-series(j-2)
  # elif n <= 1:
  #   return n
  # else:
  #   return sum-series(n-1) + sum-series(n-2)