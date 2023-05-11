# input: an array of integers (nums) & an integer (target)
# output: indexes of two numbers that add up to target

# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


# example1:
# input: nums = [2,7,11,15], target = 9
# output: [0,1]

# nums[0] + nums[1] == 9, we return [0, 1].

# example2:
# input: nums = [3,2,4], target = 6
# output: [1,2]

# solution:
class Solution(object):
  def twoSum(self, nums, target):
    # create empty array to place indexes
    output = []
    # loop through each num array
    for i in range(0, len(nums)-1):
      # loop array again to check num next to i
      for j in range(i+1, len(nums)):
        # check if nums up to target
        if nums[i] + nums[j] == target:
          # add nums to output array
          output.append(i)
          output.append(j)
    # return array
    return output

print(Solution().twoSum([2, 7, 11, 15], 9))