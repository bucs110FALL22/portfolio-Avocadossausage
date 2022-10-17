

def percentage_to_letter(score = 0):
  score = int(input("Enter a score: "))
  letter = ""
  if score >= 90:
    letter = "A"
  elif score < 90 and score >= 80:
    letter = "B"
  elif score < 80 and score >= 70:
    letter = "C"
  elif score < 70 and score >= 60:
    letter = "D"
  else: 
    letter = "F"
  
  return letter

def is_passing(letter):
  if letter == "A":
    return True
  elif letter == "B":
    return True
  elif letter == "C":
    return True
  else:
    return False

result = is_passing(percentage_to_letter())
print(result)
