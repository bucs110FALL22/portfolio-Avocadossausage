def multiplier(n1, n2):
  accumulator = 0
  for i in range(n1):
    accumulator = accumulator + n2
  return accumulator

def exponent_raise(number, exponent):
  raiser = 1
  for i in range(exponent):
    raiser = raiser * number
  return raiser

def square(num):
 exponent_raise(2, num)