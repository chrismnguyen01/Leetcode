# 1004. Max Consecutive Ones III
https://leetcode.com/problems/max-consecutive-ones-iii/?envType=study-plan-v2&envId=leetcode-75

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

### Example 1:

```
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
```

### Example 2:

```
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
```

### Constraints:

```
1 <= nums.length <= 105
nums[i] is either 0 or 1.
```

```python
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Left side of window = 0
        l = 0
        # For each element
        for r in range(len(nums)):
            # If right of window is 0 subtract 1 from k (we're flipping)
            if nums[r] == 0:
                k -= 1
            # If k is negative (we've run out of 0s to flip) move the left side
            if k < 0:
                # If the left of the window is 0 then we gain a flip back
                if nums[l] == 0:
                    k += 1
                l += 1
        
        # The size of the window is the max consecutive
        return r-l+1
```