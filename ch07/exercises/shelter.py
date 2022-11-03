import time

class Animal:
  def __init__(self, name, type):
    self.id = time.strftime("%d/%m/%Y")
    self.name = name
    self.type = type
    self.arrived = time.strftime("%d/%m/%Y")
    self.adopted = None

def set_adopted(self):
  self.adopted = time.strftime("%d/%m/%Y")

def main():
  fido = Animal("fido", "cat")
  fido.setAdopted()
  print()
main()