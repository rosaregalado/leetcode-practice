# input: the heads of 2 sorted linked lists (l1 and l2)
# output: one merged linked list 

# Merge the two lists in a one sorted list. 
# The list should be made by splicing together the nodes of the first two lists
# Return the head of the merged linked list.

# example1:
# input: list1 = [1,2,4], list2 = [1,3,4]
# output: [1,1,2,3,4,4]

# example2:
# input: list1 = [], list2 = []
# output: []

# example3:
# input: list1 = [], list2 = [0]
# output: [0]

# constraints:
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.


# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

# recursive method
class Solution(object):
  def mergeTwoLists(self, l1, l2):
    # check if both lists are non-empty
    if l1 and l2:
      # if l1 is greater than l2
      if l1.val > l2.val:
        l1, l2 = l2, l1
      # merge list remainders behind l1
      # l1 is smaller than l2
      l1.next = self.mergeTwoLists(l1.next, l2)
    return l1 or l2



# class Solution2(object):
#   def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
      
#     # Base cases stop condition
#     if not l1 and not l2:
#       # both l1 and l2 are empty list
#       return None
    
#     elif not l1:
#       # l1 is empty, directly return l2
#       return l2
    
#     elif not l2:
#       # l2 is empty, directly return l1
#       return l1
      
#     # General cases
#     # Compare node value and merge
    
#     if l1.val < l2.val:
#       # l1 is smaller than l2
#       l1.next = self.mergeTwoLists(l1.next, l2)
#       return l1
    
#     else:
#       # l2 is smaller than l1
#       l2.next = self.mergeTwoLists(l1, l2.next)
#       return l2

