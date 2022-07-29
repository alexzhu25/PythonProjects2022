# passwordgenerator.py
# use to generate random passwords

import random
import string

random.seed()


# ask user to input password length
passLength = 0 # set temp value for password length

while(True):
  passLength = input("How long should the password be?\n")
  try: # try converting the input value into an integer
    passLength = int(passLength)
  except: # if input was not an integer, print error and ask for input again
    print("Error: Input was not an integer.")
    continue
  if passLength <= 0: # check if integer is greater than zero, return error and ask for input again if not greater than zero
    print("Error: The integer must be greater than zero.")
    continue
  break # if input was integer greater than zero, break loop and move to next section


# ask user if want to use characters, numbers, or special characters in password
possibleCharacters = "" # set empty string for possible values for password characters and add values later

while(True):
  ynLetters = input("Do you want to use alphabetical letters in the password? (y/n)\n")
  if ynLetters == "y":
    possibleCharacters += string.ascii_letters # if user requests letters, add letters to possibleCharacters
    break
  elif ynLetters == "n":
    break
  else:
    print("Incorrect input.")
    continue

while(True):
  ynNumbers = input("Do you want to use numbers in the password? (y/n)\n")
  if ynNumbers == "y":
    possibleCharacters += "0123456789"
    break
  elif ynNumbers == "n":
    break
  else:
    print("Incorrect input.")
    continue

while(True):
  ynSpecial = input("Do you want to use special characters in the password? (y/n)\n")
  if ynSpecial == "y":
    possibleCharacters += "!@#$%^&*()_+-="
    break
  elif ynSpecial == "n":
    break
  else:
    print("Incorrect input.")
    continue


# generate random characters based on input length and character selections and combine into password
password = "" # set empty string for password
for i in range(passLength):
  c = random.choice(possibleCharacters)
  password += c


# print resulting password
print("Password: " + password)