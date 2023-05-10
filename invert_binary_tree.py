# Given the root of a binary tree, invert the tree, and return its root.

# input: root of binary tree (array)

# output: inverted root of binary tree (array)

# example:
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution(object):
  def invertTree(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """

    # base case
    if root is None:
      return None

    # swap left and right sub-trees
    root.left, root.right = root.right, root.left
    # invert the left sub-tree recursively
    self.invertTree(root.left)
    # invert the right sub-tree recursively
    self.invertTree(root.right)

    # return root array
    return root



def print_tree(node):
  if node is None:
    return
  print_tree(node.left)
  print(node.val)
  print_tree(node.right)

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)

root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

solution = Solution()
inverted_root = solution.invertTree(root)
print_tree(inverted_root)
# expected output: 9 7 6 4 3 2 1

