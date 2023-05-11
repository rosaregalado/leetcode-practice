# input: string of words
# output: integer

# given a string s consisting of some words separated by some number of spaces
# return the length of the last word in the string


# example1:
# input:  s = "Hello World"
# output: 5
# (The last word is 'world' with length 5)


# example2:
# input: s = "   fly me   to   the moon  "
# output: 4
# (The last word is 'moon' with length 4)


# constraints:
# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '
# There will be at least one word in s


# solution:
class Solution(object):
  def lengthOfLastWord(self, s: str) -> int:
    # split the string (sentence)
    sentence = s.split()
    # return length of the last word in sentence
    return(len(sentence[-1]))