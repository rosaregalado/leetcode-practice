# Given two arrays a and b of numbers and a target value t, 
# find a number from each array whose sum is closest to t.

# input: two arrays - a & b, t = target value

# output: array of two numbers whose sum is closest to t

def find_closest_sum(a, b, t):
  # initialize closest sum to large number (positive infinity)
  closest_sum = float('inf')
  # create an empty array to store the result
  result = []

  # iterate over each element in array a
  for num_a in a:
    # iterate over each element in array b
    for num_b in b:
      # calculate the sum of the current pair of nmbers
      current_sum = num_a + num_b
      # calculate the difference between the sum and the target value
      diff = abs(t- current_sum)

      # check if the difference is smaller than the difference of the previous sum
      if diff < abs(t - closest_sum):
        # if yes, update the closest sum with the current sum
        closest_sum = current_sum
        # and update result array with the current pair of numbers
        result = [num_a, num_b]

  # return result array
  return result






a = [9, 13, 1, 8, 12, 4, 0, 5]  
b = [3, 17, 4, 14, 6]  
t = 20  
# output ⇒  [13, 6] or [4, 17] or [5, 14]
print(find_closest_sum(a, b, t))
