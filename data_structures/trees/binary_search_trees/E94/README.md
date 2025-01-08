# 94. Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal/description/?envType=problem-list-v2&envId=depth-first-search

Given the root of a binary tree, return the inorder traversal of its nodes' values.

### Example 1:

```
Input: root = [1,null,2,3]

Output: [1,3,2]

Explanation:

```

### Example 2:

```
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [4,2,6,5,7,1,3,9,8]

Explanation:

```

### Example 3:

```
Input: root = []

Output: []

```

### Example 4:

```
Input: root = [1]

Output: [1]
```

### Constraints:

```
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
```

## Code

### Recursive

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:        
        def helper(root, r):
            if not root:
                return r
            helper(root.left, r)
            r.append(root.val)
            helper(root.right, r)

            return r
        
        res = []
        return helper(root, res)
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()  # the last element
            if node:
                if visited:
                    res.append(node.val)
                else:  # inorder: left -> root -> right
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))
        return res
```