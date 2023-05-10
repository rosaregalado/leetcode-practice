# Given an array a of n numbers and a count k find the k largest values in the array a.
# Example: a=[5, 1, 3, 6, 8, 2, 4, 7], k=3  ⇒  [6, 8, 7]

# input: a = array of numbers, k = number of elements to return
# output: array of numbers

def find_largest_k_values(arr, k):
  # sort the array into descending order to get the largest values to the front of array
  sorted_array = sorted(arr, reverse=True)
  # initialize an empty array to store the largest values
  largest_values = []

  # iterate over the sorted array up to index k
  for i in range(k):
    # append the element to largest values array
    largest_values.append(sorted_array[i])
  
  # return largest values array
  return largest_values



a = [5, 1, 3, 6, 8, 2, 4, 7]
k = 3  
# output ⇒  [8, 7, 6]
result = find_largest_k_values(a, k)
print(result)

