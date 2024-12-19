# Binary Search Trees

## Description

A Binary Search Tree (BST) is a data structure where each node has at most two children: a left child and a right child. In a BST:

The left subtree of a node contains only nodes with values less than the node's value.
The right subtree contains only nodes with values greater than the node's value.
This property allows for efficient searching, insertion, and deletion operations, typically with an average time complexity of O(logn).

BSTs are commonly used in scenarios like:
-Fast searching and sorting.
-Implementing ordered sets and maps.

## Operations

1. Insertion:
    - Average case: O(log n)
    - In a balanced tree, the depth of the tree is log n, so we can find the appropriate position for the new node in logarithmic time.
    - Worst case: O(n)
    - In the worst case, when the tree is unbalanced (e.g., all nodes are inserted in ascending or descending order), the tree degenerates into a linked list, and the insertion takes linear time.
2. Search:
    - Average case: O(log n)
    - In a balanced tree, the search operation traverses the height of the tree, which is logarithmic.
    - Worst case: O(n)
    - In the worst case (when the tree is unbalanced and resembles a linked list), the search operation may require traversing all nodes in the tree.
3. Deletion:
    - Average case: O(log n)
    - In a balanced tree, the node to be deleted is found in O(log n), and adjusting pointers (especially for nodes with one or two children) also takes logarithmic time.
    - Worst case: O(n)
    - If the tree is unbalanced, the height could be O(n), and finding the node to delete or adjusting pointers after deletion might take linear time.
4. In-order Traversal (and other traversals like Pre-order and Post-order):
    - Time complexity: O(n)
    - All tree traversal methods (in-order, pre-order, and post-order) visit each node exactly once. Therefore, the time complexity for all these traversal methods is linear in the number of nodes.
5. Finding the Minimum Node:
    - Average case: O(log n)
    - In a balanced tree, the minimum node is found by following the left child pointers, which takes logarithmic time.
    - Worst case: O(n)
    - In the worst case, the tree is unbalanced (like a linked list), and finding the minimum node requires traversing all the nodes.
6. Balancing the Tree:
    - Time complexity: O(n)
    - To balance the tree, we first need to perform an in-order traversal to get all the nodes in sorted order, which takes O(n). After that, we rebuild the tree from the sorted nodes, which also takes O(n). So, the overall time complexity is O(n).

Operation            | Average Case | Best Case
:---:                | :---:        | :---:
Insertion            | O(logn)      | O(n)
Search               | O(log n)     | O(n)
Deletion             | O(log n)     | O(n)
In-order Traversal   | O(n)         | O(n)
Pre-order Traversal  | O(n)         | O(n)
Post-order Traversal | O(n)         | O(n)
Find Minimum         | O(log n)     | O(n)
Balancing            | O(n)         | O(n)

## Shell Code

```python
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert node
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursively(self.root, key)

    def _insert_recursively(self, node, key):
        # If the value is less than the current node
        if key < node.value:
            # If no left node then add to the left
            if node.left is None:
                node.left = Node(key)
            # Else go left
            else:
                self._insert_recursively(node.left, key)
        # Else if the value is greater than the current node
        else:
            # If no right node then add to the right
            if node.right is None:
                node.right = Node(key)
            # Else go right
            else:
                self._insert_recursively(node.right, key)

    # Search for a node with given key
    def search(self, key):
        return self._search_recursively(self.root, key)

    def _search_recursively(self, node, key):
        # If we are at the end of the tree or the key return it
        if node is None or node.value == key:
            return node
        # If the key is less then the current node search left
        elif key < node.value:
            return self._search_recursively(node.left, key)
        # Else search right
        else:
            return self._search_recursively(node.right, key)

    # Inorder Traversal (left, root, right)
    def inorder_traversal(self):
        result = []
        self._inorder_recursively(self.root, result)
        return result

    def _inorder_recursively(self, node, result):
        if node:
            self._inorder_recursively(node.left, result)
            result.append(node.value)
            self._inorder_recursively(node.right, result)

    # Pre-order Traversal (root, left, right)
    def preorder_traversal(self):
        result = []
        self._preorder_recursively(self.root, result)
        return result

    def _preorder_recursively(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_recursively(node.left, result)
            self._preorder_recursively(node.right, result)

    # Post-order Traversal (left, right, root)
    def postorder_traversal(self):
        result = []
        self._postorder_recursively(self.root, result)
        return result

    def _postorder_recursively(self, node, result):
        if node:
            self._postorder_recursively(node.left, result)
            self._postorder_recursively(node.right, result)
            result.append(node.value)

    # Find the minimum value node (leftmost node)
    def find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Delete a node
    def delete(self, key):
        self.root = self._delete_recursively(self.root, key)

    def _delete_recursively(self, root, key):
        # Base case
        if root is None:
            return root

        # If key is smaller than root's value, then go to left subtree
        if key < root.value:
            root.left = self._delete_recursively(root.left, key)
        
        # If key is greater than root's value, then go to right subtree
        elif key > root.value:
            root.right = self._delete_recursively(root.right, key)
        
        # If key is the same as root's value, this is the node to be deleted
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            root.value = self.find_min(root.right).value
            
            # Delete the inorder successor
            root.right = self._delete_recursively(root.right, root.value)

        return root

    # Balancing the tree using a sorted array
    def balance(self):
        # Convert the BST to a sorted array
        sorted_nodes = self.inorder_traversal()
        
        # Rebuild the tree from the sorted array
        self.root = self._sorted_array_to_bst(sorted_nodes)

    def _sorted_array_to_bst(self, sorted_nodes):
        if not sorted_nodes:
            return None
        mid = len(sorted_nodes) // 2
        node = Node(sorted_nodes[mid])
        node.left = self._sorted_array_to_bst(sorted_nodes[:mid])
        node.right = self._sorted_array_to_bst(sorted_nodes[mid+1:])
        return node
```