# 101. Symmetric Tree
https://leetcode.com/problems/symmetric-tree/?envType=problem-list-v2&envId=depth-first-search

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

### Example 1:

```
Input: root = [1,2,2,3,4,4,3]
Output: true
```

### Example 2:

```
Input: root = [1,2,2,null,3,null,3]
Output: false
```

### Constraints:

```
The number of nodes in the tree is in the range [1, 1000].
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.helper(root.left, root.right)

    def helper(self, left, right):
        # If both roots are None they're the same
        if left == None and right == None:
            return True
        # If one of the roots is None and the other isn't they're not the same
        if left == None or right == None:
            return False
        # If the roots' values are different they are not the same
        if left.val != right.val:
            return False
        # Compare left child of left root and right child of right root, and then the other two
        return self.helper(left.left, right.right) and self.helper(left.right, right.left)
```