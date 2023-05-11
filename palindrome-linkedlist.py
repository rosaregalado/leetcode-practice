# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


# input: linkedlist
# output: boolean (true or false)

# example1:
# input: head = [1, 2, 2, 1]
# output: true

# example 2:
# Input: head = [1,2]
# Output: false

"""
:type head: ListNode
:rtype: bool
"""       
        
class Solution:
  def isPalindrome(self, head: ListNode) -> bool:
    # create empty list
    new_list = []
    # set node head
    node = head
    # while loop
    while node:
      # append node values to list
      new_list.append(node.val)
      # assign current node to next node
      node = node.next
    node = head
    while node:
      # if last value is not the curr node value
      if new_list[-1] != node.val:
        return False
      # remove value
      new_list.pop()
      # assign next node
      node = node.next
    return True