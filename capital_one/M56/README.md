# Merge Intervals
https://leetcode.com/problems/merge-intervals/description/

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

### Example 1:

```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
```

### Example 2:

```
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

### Example 3:

```
Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.
```

### Constraints:

```
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
```

## Code

```python
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = []
        intervals.sort(key=lambda x: x[0])

        curStart = intervals[0][0]
        curEnd = intervals[0][1]

        for start, end in intervals:
            if start <= curEnd:
                curEnd = max(curEnd, end)
            else:
                ret.append([curStart, curEnd])
                curStart = start
                curEnd = end

        ret.append([curStart, curEnd])
        return ret
```