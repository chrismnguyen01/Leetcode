# 98. Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/description/?envType=problem-list-v2&envId=depth-first-search

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

### Example 1:

```
Input: root = [2,1,3]
Output: true
```

### Example 2:

```
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```

### Constraints:

```
The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
```

## Code

### Recursion

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low, high):
            # Base case: an empty node is valid
            if not node:
                return True
            
            # Check if the current node's value is within the valid range
            if not (low < node.val < high):
                return False
            
            # Recursively check the left subtree with updated upper bound
            # and the right subtree with updated lower bound
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        
        # Start with the full range of valid values for the root
        return validate(root, float('-inf'), float('inf'))
```

### Stack

```python
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def isValidBST(self, root: Optional[TreeNode]) -> bool:
            if not root:
                return True
            
            # Stack to store the nodes and their valid range (low, high)
            stack = [(root, float('-inf'), float('inf'))]
            
            while stack:
                node, low, high = stack.pop()
                
                if not node:
                    continue
                
                # Check if the current node's value is within the valid range
                if not (low < node.val < high):
                    return False
                
                # Push the right child first (it will be processed later due to stack's LIFO nature)
                if node.right:
                    stack.append((node.right, node.val, high))
                
                # Push the left child next (it will be processed sooner than the right child)
                if node.left:
                    stack.append((node.left, low, node.val))
            
            return True
    ```