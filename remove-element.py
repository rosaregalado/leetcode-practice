# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

# if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. 
# It does not matter what you leave beyond the first k elements.
# Return k after placing the final result in the first k slots of nums.
# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.


# input: integers array and a target integer
# output: integer that represents how many integers left in array after removal of target int

# example1:

# nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]

# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).




class Solution(object):
  def removeElement(self, nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    # init index count for the remaining list of integers
    x = 0
    # iterate through integer list
    for i in range(len(nums)):
      # if the current index is NOT the value
      if(nums[i]!=val):
        # copy it to its corresponding index
        nums[x] = nums[i]
        # keep incrementing the index count
        x += 1
    # return index count
    return(x)

