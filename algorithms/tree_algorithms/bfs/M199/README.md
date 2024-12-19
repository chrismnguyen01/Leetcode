# 199. Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/?envType=study-plan-v2&envId=leetcode-75

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

### Example 1:

```
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
```

### Example 2:

```
Input: root = [1,2,3,4,null,null,null,5]
Output: [1,3,4,5]
```

### Example 3:

```
Input: root = [1,null,3]
Output: [1,3]
```

### Example 4:

```
Input: root = []
Output: []
```

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = []
        # If no root return empty
        if root is None:
            return ans
        
        # Start with the root
        temp = deque([root])

        # While the queue still has elements
        while temp:
            # Get the length of the queue
            l = len(temp)
            val = 0

            # Iterate through the whole queue
            # Since the queue is left to right, the final value of val
            # Will be the right most child of this level
            for _ in range(l):
                # Get the first element
                node = temp.popleft()
                val = node.val

                # If it has a left child add it to the queue
                if node.left:
                    temp.append(node.left)
                if node.right:
                # If it has a rigth child add it to the queue
                    temp.append(node.right)
            
            # Add the right most child to the return list
            ans.append(val)

        return ans
```