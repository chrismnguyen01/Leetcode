# Merge Sort

## Description

Merge Sort is also a divide-and-conquer algorithm. It works by dividing the array into two halves, recursively sorting both halves, and then merging the sorted halves to produce the final sorted array.

## Time Complexity
Best/Average/Worst case: O(n log n)
Space Complexity: O(n) (requires extra space for merging)
Use Case: Ideal for situations where you cannot afford to have O(n²) time complexity, especially with large datasets or external sorting (when the data doesn't fit in memory).
Advantages:
Stable sorting (the relative order of equal elements is preserved).
Consistent O(n log n) performance regardless of input.
Disadvantages:
Requires O(n) extra space, which may be a limitation for large datasets.
Slower for small datasets compared to other algorithms like Quick Sort or Insertion Sort.

```python
def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        mergesort(left_half)
        mergesort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

arr = [12, 11, 13, 5, 6, 7]
mergesort(arr)
print(arr)  # Output: [5, 6, 7, 11, 12, 13]
```