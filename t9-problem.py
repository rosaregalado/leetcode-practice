# input - given a string of digits 2 to 9 a user has presented on an old T9 phone keypad
# output - return a list of all letter combinations they could've been trying to type


letters_dict = {
  '2': ['a', 'b', 'c'],
  '3': ['d', 'e', 'f'],
  '4': ['g', 'h', 'i'],
  '5': ['j', 'k', 'l'],
  '6': ['m', 'n', 'o'],
  '7': ['p', 'q', 'r', 's'],
  '8': ['t', 'u', 'v'],
  '9': ['w', 'x', 'y', 'z']
}


def keypad_letters(keys, string=""):
  # initialize empty list to store combinations of letters formed
  combinations = []
  # get the first key from the list
  current_key= keys[0]

  # iterate over each letter in the current key
  for letter in letters_dict[current_key]:
    # if there's only 1 key left in the keys list
    if (len(keys) == 1):
      # add current letter to the string and append it to combinations list
      combinations.append(string + letter)
    else:
      # else if there are more keys left in the list, call the function itself with the rest of the keys after the first key
      combinations += keypad_letters(keys[1:], string + letter)
  
  # return the list that contains all possible combinations of letters
  return combinations




print(keypad_letters('23'))
print(keypad_letters('568'))