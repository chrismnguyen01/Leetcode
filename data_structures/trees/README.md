

traversal

inorder
recursive
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    def inOrderTraversal(node):
        nonlocal first, second, prev
        
        if not node:
            return
        
        # Traverse the left subtree
        inOrderTraversal(node.left)
        
        # Do something
        
        # Traverse the right subtree
        inOrderTraversal(node.right)
```