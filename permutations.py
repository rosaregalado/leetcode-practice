# Given an array nums of distinct integers, return all the possible permutations. 
# You can return the answer in any order.


# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

def permute(nums):
  # initialize empty list to store permutations
  result = []
  # call the backtrack function to generate all permutations
  backtrack(nums, [], result)
  return result

def backtrack(nums, path, result):
  # base case:
  # if the current path has the same length as the input array
  if len(path) == len(nums):
    # we have complete permutation, add a copy of the path to the result list
    result.append(path.copy())
    return

  for num in nums:
    # check if the current number is not in current path
    if num not in path:
      # add the number to the current path
      path.append(num)
      # recursively call backtrack with the updated path
      backtrack(nums, path, result)
      # remove the last added number from the path
      path.pop()


nums = [1, 2, 3]
print(permute(nums))
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
