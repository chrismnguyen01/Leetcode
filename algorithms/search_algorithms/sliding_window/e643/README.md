# 643. Maximum Average Subarray 1
https://leetcode.com/problems/maximum-average-subarray-i/

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

### Example 1:

```
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
```

### Example 2:

```
Input: nums = [5], k = 1
Output: 5.00000
```

### Constraints:

```
n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
```

### Solution:

```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxAverage = float('-inf')
        # For each element until the beginning of the last window
        for i in range(0, len(nums) - k):
            sum = 0
            # Sum the window
            for j in range(0, k):
                sum += nums[i + j]
            if sum/k > maxAverage:
                maxAverage = sum/k
        
        return maxAverage
```