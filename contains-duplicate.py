# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# input: integers array
# output: boolean (true or false)

# example1:
# Input: nums = [1,2,3,1]
# Output: true

# example2:
# Input: nums = [1,2,3,4]
# Output: false


class Solution:
  def containsDuplicate(self, nums) -> bool:
    """
      :type nums: List[int]
      :rtype: bool
    """
    # create an object
    S = set()

    # iterate through nums
    for num in nums:
      # if num exists in set
      if num in S: 
        return True
      # else, add num to obj
      S.add(num)

    # return false if every element is distinct
    return False