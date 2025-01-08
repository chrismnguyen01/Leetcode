# 79. Word Search
https://leetcode.com/problems/word-search/description/?envType=problem-list-v2&envId=depth-first-search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

### Example 1:

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
```

### Example 2:

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
```

### Example 3:

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
```

### Constraints:

```
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
```

## Code

```python
class Solution:
    def exist(self, board, word):
        def backtrack(word, i, j, m, n):
            # If the letter is not in self.l position in the word then quit this recursion
            if board[i][j] != word[self.l]:
                return
            # Store which cells we've already visited so we don't dupicate backtrack() calls
            visited.add((i, j))
            # Go to the next letter in word
            self.l += 1
            # If we reached the length of word then we know we've found the word
            if self.l == len(word):
                self.is_found = True
                return 
            # Iterate through each direction from this cell
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                i1, j1 = i + di, j + dj
                # If we haven't visited the cell then recursively call backtrack() on it
                if 0 <= i1 < m and 0 <= j1 < n and (i1, j1) not in visited:
                    backtrack(word, i1, j1, m, n)
                    if self.is_found:
                        return 
            # Once we finish DFS on this cell remove it from visited
            visited.remove((i, j))
            # Go back one letter
            self.l -= 1
        
        if not board or not board[0]:
            return False
        if word == '':
            return True
        m, n = len(board), len(board[0])
        self.is_found = False
        self.l = 0
        visited = set()
        # Iterate through each cell
        for i in range(m):
            for j in range(n):
                backtrack(word, i, j, m, n)
                if self.is_found:
                    return True
        return False
```