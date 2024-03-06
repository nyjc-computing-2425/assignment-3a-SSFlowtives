nric = input('Enter an NRIC number: ')

# Type your code below
prefix = nric[0].upper()
numbers = nric[1:8]
suffix = nric[8:].upper()
bool = False

dictST = "JZIHGFEDCBA"
dictFG = "XWUTRQPNMLK"

if prefix in "STFG":
  if numbers.isdigit():
    if len(suffix) == 1 and suffix.isalpha():
      check = 2*int(nric[1]) + 7*int(nric[2]) + 6*int(nric[3]) + 5*int(nric[4]) + 4*int(nric[5]) + 3*int(nric[6]) + 2*int(nric[7])
      if prefix in "TG":
        check += 4
      check %= 11
      if prefix in "ST":
        if dictST[check] == suffix:
          bool = True
      else:
        if dictFG[check] == suffix:
          bool = True

if bool:
  print("NRIC is valid.")
else:
  print("NRIC is invalid.")