
def rstar_pyramid():
  rows = int(input("Enter a number of rows:  "))
  for i in range(rows):
    for n in range(i+1):
      print( "*" * rows, end = "")
      print("\n")
      rows -= 1

rstar_pyramid()


def star_pyramid():
  starcount = 1
  rows = int(input("Enter a number of rows:  "))
  for i in range(rows):
    for n in range(i + 1):
      print( "*" * starcount, end = "")
      starcount += 1
      print("\n")
star_pyramid()