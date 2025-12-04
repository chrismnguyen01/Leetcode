# 55. Jump Game
https://leetcode.com/problems/jump-game/?envType=study-plan-v2&envId=top-interview-150

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

### Example 1:

```
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

### Example 2:

```
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
```

### Constraints:

```
1 <= nums.length <= 104
0 <= nums[i] <= 105
```

## Code

### Dynamic Programming

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True  # Starting point is reachable

        for i in range(n):
            if dp[i]:  # If i is reachable
                for j in range(i + 1, min(i + nums[i] + 1, n)):
                    dp[j] = True  # Mark reachable indices

        return dp[n - 1]  # Return whether the last index is reachable
```

### Greedy

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False  # Can't reach this index
            farthest = max(farthest, i + nums[i])  # Update the farthest reachable index
            if farthest >= len(nums) - 1:
                return True  # If we can reach or surpass the last index
        return False
```

