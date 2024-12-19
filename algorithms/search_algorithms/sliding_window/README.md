# Sliding Window

## Description

The sliding window algorithm is a technique used to solve problems involving sequences (such as arrays or lists) by maintaining a "window" of elements that moves over the sequence in a linear fashion. The window can be of fixed or variable size, and it "slides" one element at a time.

The main idea is to reduce the number of calculations by reusing previous results as the window moves, instead of recalculating for every possible subarray or subsequence. This improves efficiency, often reducing time complexity from O(n^2) to O(n) in problems where examining each subarray individually would be too slow.

Common use cases for the sliding window algorithm include:

Finding the maximum or minimum sum in a subarray of fixed size.
Finding the longest substring with certain conditions (e.g., no repeating characters).
Solving problems related to averages, sums, or counts over continuous subarrays or subsequences.

## Shell Code

### 'Stateless'

[e643](/algorithms/search_algorithms/sliding_window/e643/README.md)

```python
class Solution:
    def sliding_window(self, arr, window_size):
        """
        A general sliding window function to process the array with a fixed window size.
        
        :param arr: List of elements (numbers, strings, etc.)
        :param window_size: Size of the sliding window
        :return: List of results based on the window operation (sum, max, min, etc.)
        """
        if len(arr) < window_size:
            return []

        result = []

        # For each element from 0 to the last window
        for i in range(0, len(arr) - window_size):
            for j in range(0, window_size):
                # Do something
```

### Running Count from Last Window

[m1456](/algorithms/search_algorithms/sliding_window/m1456/README.md)

```python
class Solution:
    def sliding_window(self, arr, window_sizet):
        
        m = cur = 0
        
        # Calculate first window
        for i in range(0, k):
            # Do something

        # Iterate through each index after initial window until end
        for i in range(k, len(s)):
            # Gaining something in new index
            # Losing something from last window
            if s[i] and not s[i-k]:
                cur += 1
            # Losing something in new index
            # Gaining something from last window
            if not s[i] and s[i-k]:
                cur -= 1
            
            # Get the max of this wondow or the maximum
            m = max(m, cur)
        return m
```

### Different Cases to Move Left and Right pointer

[m1493](/algorithms/search_algorithms/sliding_window/m1493/README.md)

```python
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zcount = 0
        l = 0
        m = 0

        # For each element (this is moving the right pointer through the array)
        for r in range(len(nums)):
            if something
            
            # Condition to move the left pointer
            while something:
                if condition to move left:
                    l += 1
            
            # Return either 0 or the size of the window
            m = max(m, r - l)
        
        return m
```