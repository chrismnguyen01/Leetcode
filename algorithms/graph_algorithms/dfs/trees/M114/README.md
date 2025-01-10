# 114. Flatten Binary Tree to Linked List
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/?envType=problem-list-v2&envId=depth-first-search

ven the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

### Example 1:

```
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
```

### Example 2:

```
Input: root = []
Output: []
```

### Example 3:

```
Input: root = [0]
Output: [0]
```

### Constraints:

```
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
```

## Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.previous_right = None
        def helper(root = root):
            if root:
                # Go down right tree first
                helper(root.right)
                # Then left tree
                helper(root.left)
                # Keep track of this node in previous_right (since in the next step this node is the previous one)
                # Set this node's right to the previous node
                root.right, self.previous_right = self.previous_right, root
                # Set this node's left to None
                root.left = None
        helper()     
```