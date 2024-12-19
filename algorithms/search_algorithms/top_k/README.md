# Min-Heap (Priority Queue):

## Description

Approach: Use a min-heap to maintain the K largest (or smallest) elements as you traverse through the array. If the heap grows larger than K, remove the smallest (or largest) element.
Time Complexity: O(n log K), where n is the number of elements in the dataset. This is more efficient than sorting when K is much smaller than n.
Pros: Efficient when K is small compared to n.
Cons: More complex to implement than sorting.
Example: Find the K largest elements from an array using a min-heap.

```python
import heapq

def top_k_largest(arr, k):
    min_heap = arr[:k]
    heapq.heapify(min_heap)  # Create a min-heap from the first k elements
    for num in arr[k:]:
        if num > min_heap[0]:
            heapq.heappushpop(min_heap, num)
    return min_heap
```