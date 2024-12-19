# Sliding Window

## Description

Blah blah blah

## Shell Code

### 'Stateless'

e643

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

        # for each element from 0 to the last window
        for i in range(0, len(arr) - window_size):
            for j in range(0, window_size):
                # do something
```

### Running Count from Last Window

m1456

```python
class Solution:
    def sliding_window(self, arr, window_sizet):
        
        m = cur = 0
        
        # calculate first window
        for i in range(0, k):
            #do something

        # iterate through each index after initial window until end
        for i in range(k, len(s)):
            # gaining something in new index
            # losing something from last window
            if s[i] in vowels and not s[i-k]:
                cur += 1
            # losing something in new index
            # gaining something from last window
            if not s[i] and s[i-k]:
                cur -= 1
            
            # get the max of this wondow or the maximum
            m = max(m, cur)
        return m
```