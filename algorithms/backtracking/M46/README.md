# Permutations
https://leetcode.com/problems/permutations/description/

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

### Example 1:

```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

### Example 2:

```
Input: nums = [0,1]
Output: [[0,1],[1,0]]
```

### Example 3:

```
Input: nums = [1]
Output: [[1]]
```

### Constraints:

```
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
```

## Code

```python
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        visited = [False] * len(nums)
        paths = []

        def dfs(currPath):
            if len(currPath) == len(nums):
                paths.append(currPath[:])
                return
            
            for index, val in enumerate(nums):
                if not visited[index]:
                    visited[index] = True
                    currPath.append(val)
                    dfs(currPath)
                    currPath.pop()
                    visited[index] = False

        dfs([])

        return paths
```