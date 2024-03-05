nric = input('Enter an NRIC number: ')

# Type your code below
prefix = nric[0].upper()
numbers = nric[1:8]
suffix = nric[8:].upper()
bool = False

dictST = {
  'J' : 0, 'Z' : 1, 'I' : 2, 'H' : 3, 'G' : 4, 'F' : 5, 'E' : 6, 'D' : 7, 'C' : 8, 'B' : 9, 'A' : 10
}
dictFG = {
  'X' : 0, 'W' : 1, 'U' : 2, 'T' : 3, 'R' : 4, 'Q' : 5, 'P' : 6, 'N' : 7, 'M' : 8, 'L' : 9, 'K' : 10
}

if prefix in ['S', 'T', 'F', 'G']:
  if numbers.isdigit():
    if len(suffix) == 1 and suffix.isalpha():
      check = 2 * int(nric[1]) + 7 * int(nric[2]) + 6 * int(nric[3]) + 5 * int(nric[4]) + 4 * int(nric[5]) + 3 * int(nric[6]) + 2 * int(nric[7])
      if prefix in ['T', 'G']:
        check += 4
      check %= 11
      if prefix in ['S', 'T']:
        if dictST[suffix] == check:
          bool = True
      else:
        if dictFG[suffix] == check:
          bool = True

if bool:
  print("NRIC is valid.")
else:
  print("NRIC is invalid.")