# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

# input: sorted array of distinct integers and a target value
# output: index of target value

# example1:
# input: nums = [1,3,5,6], target = 5
# output: 2 (5 is at index 2)

# example2:
# input: nums = [1,3,5,6], target = 2
# output: 1 (2 would be inserted at index 1)

# binary search: a search algorithm that finds the position of a target value within a sorted array
# Binary search compares the target value to the middle element of the array


# recursive method
# uses binary search 
class Solution(object):
  def searchInsert(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # binary search O(log N)
    if len(nums) == 0:
      return 0
    N = len(nums)
    midpoint = int(N / 2)
    # check if target is the midpoint value
    if nums[midpoint] == target:
      return midpoint
    # check left side of array
    elif nums[midpoint] > target:
      # calls the original function (recursive)
      return self.searchInsert(nums[:midpoint],target)
    else:
      # check right side of array
      res = self.searchInsert(nums[midpoint+1:],target)
      # return the index where it would be if it were inserted in order
      return res + midpoint + 1


print(Solution().searchInsert([1,3,5,6], 5))