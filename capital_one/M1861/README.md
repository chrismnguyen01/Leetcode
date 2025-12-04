# Rotating the Box
https://leetcode.com/problems/rotating-the-box/description/

You are given an m x n matrix of characters boxGrid representing a side-view of a box. Each cell of the box is one of the following:

A stone '#'
A stationary obstacle '*'
Empty '.'
The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

It is guaranteed that each stone in boxGrid rests on an obstacle, another stone, or the bottom of the box.

Return an n x m matrix representing the box after the rotation described above.

### Example 1:

```
Input: boxGrid = [["#",".","#"]]
Output: [["."],
["#"],
["#"]]
```

### Example 2:

```
Input: boxGrid = [["#",".","*","."],
["#","#","*","."]]
Output: [["#","."],
["#","#"],
["*","*"],
[".","."]]
```

### Example 3:

```
Input: boxGrid = [["#","#","*",".","*","."],
["#","#","#","*",".","."],
["#","#","#",".","#","."]]
Output: [[".","#","#"],
[".","#","#"],
["#","#","*"],
["#","*","."],
["#",".","*"],
["#",".","."]]
```

### Constraints:

```
m == boxGrid.length
n == boxGrid[i].length
1 <= m, n <= 500
boxGrid[i][j] is either '#', '*', or '.'.
```

## Code

```python
class Solution(object):
    def rotateTheBox(self, boxGrid):
        """
        :type boxGrid: List[List[str]]
        :rtype: List[List[str]]
        """
        
        ROWS = len(boxGrid)
        COLS = len(boxGrid[0])

        maxdepth = [COLS - 1] * ROWS

        for c in range(COLS - 1, -1, -1):
            for r in range(ROWS):
                if boxGrid[r][c] == '#':
                    boxGrid[r][c] = '.'
                    boxGrid[r][maxdepth[r]] = '#'
                    maxdepth[r] = maxdepth[r] - 1
                elif boxGrid[r][c] == '*':
                    maxdepth[r] = c - 1
        

        rotated = [[0] * ROWS for i in range(COLS)]

        for r in range(ROWS):
            for c in range(COLS):
                rotated[c][ROWS - r - 1] = boxGrid[r][c]
        
        return rotated
```