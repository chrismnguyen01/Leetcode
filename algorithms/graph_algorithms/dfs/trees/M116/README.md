# 116. Populating Next Right Pointers in Each Node
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/?envType=problem-list-v2&envId=depth-first-search

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
int val;
Node *left;
Node *right;
Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

### Example 1:

```
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
```

### Example 2:

```
Input: root = []
Output: []
```

### Constraints:

```
The number of nodes in the tree is in the range [0, 212 - 1].
-1000 <= Node.val <= 1000
```

## Code

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        self.previous_right = None
        def helper(root):
            # If the root exists
            if root:
                # 2 cases: If it has a left child there must be a right child to set to next
                # If this root has a next and the right child exists, the right child must be set to next left child
                if root.left:
                    root.left.next = root.right
                if root.next and root.right:
                    root.right.next = root.next.left
                # DFS left then right trees
                helper(root.left)
                helper(root.right)

        helper(root)
        return root
```