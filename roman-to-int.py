# input: roman numeral (ex: 'IV')
# output: integer (ex: 4)

# constraints:
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].


class Solution:
  def romanToInt(self, s: str) -> int:
    # store roman numerals
    roman = {
      "I":1,
      "V":5,
      "X": 10,
      "L":50,
      "C":100,
      "D":500,
      "M":1000
    }
    # initial output is zero
    res = 0
    
    # iterate through length of str         
    for i in range(len(s)):
      # if reached the end of str, go to the previous integer             
      if (i + 1 < len(s) and roman[s[i]]<roman[s[i+1]]):
        res -= roman[s[i]]
      # else, add it to the total output
      else:
        res += roman[s[i]]

    # return output
    return res
    