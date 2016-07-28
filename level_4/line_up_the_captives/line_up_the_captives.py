from math import factorial

def answer(x, y, n):
  a, b, c = x + y - 2, x-1, n - 1
  return (factorial(a) / (factorial(b) * factorial(a - b))) * order(c, a)

def order(c, a):
  if a > c:
      return 0
  if a == c:
      return 1
  if a == 1:
      return factorial(c - 1)
  else:
      return memo((c, a), lambda: order(c - 1, a - 1) + order(c - 1, a) * (c - 1),)

cache = {}
def memo(values, func, *args):
  if values not in cache:
      cache[values] = func(*args)
  return cache[values]
