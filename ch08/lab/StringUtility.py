class StringUtility:
  
  def __init__(self, string):
    self.string = string
    
  def __str__(self):
    result = self.string
    return result
    
  def vowels(self) -> str:
    count = 0
    for i in self.string:
      if(i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
        count += 1
    if count >= 5:
        return "many"
    else:
        return str(count)
  
  def bothEnds(self):
    if len(self.string) >= 2:
      theString = self.string[0] + self.string[1] + self.string[-2] + self.string[-1]
      return theString
    else:
      return ''
      
  def fixStart(self):
    if len(self.string) >= 1:
      char = self.string[0]
      for i in self.string:
        theString = self.string[1: ].replace(char, '*')

      return self.string[0] + theString
    else:
      return ''
  
  def asciiSum(self):
    ascii_sum = 0
    for i in self.string:
      ascii_sum += ord(i)
    return ascii_sum
    
  def cipher(self):
    shift_len = len(self.string)
    result = ""
    for i in range(shift_len):
      char = self.string[i]
      if char.islower():
        val1 = (((((ord(char)) - 97) + shift_len) % 26) + 97)
        result += chr(val1)
      elif char.isupper():
        val2 = (((((ord(char)) - 65) + shift_len) % 26) + 65)
        result += chr(val2)
      else:
        result += self.string[i]

    return result