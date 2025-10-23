# 295. Find Median from Data Stream
https://leetcode.com/problems/find-median-from-data-stream/description/

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

### Example 1:

```
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
```

### Constraints:

```
-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.
```

## Code

```python
import heapq

class MedianFinder:

    def __init__(self):
        # Max-heap (inverted to use heapq as a max-heap)
        self.max_heap = []  
        # Min-heap
        self.min_heap = []  

    def addNum(self, num: int) -> None:
        # Add to max-heap (invert num to simulate max-heap)
        heapq.heappush(self.max_heap, -num)

        # Move the largest element of max-heap to min-heap to balance the heaps
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        # Move the smallest element of min-heap to max-heap to balance the heaps
        if self.min_heap and -self.max_heap[0] > self.min_heap[0]:
            max_to_min = -heapq.heappop(self.max_heap)
            min_to_max = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -min_to_max)
            heapq.heappush(self.min_heap, max_to_min)

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]  # Max heap root is the median
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0  # Average of roots


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
```