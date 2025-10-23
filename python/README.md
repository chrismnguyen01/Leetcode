

### Objects are passed by reference:
When you pass an object to a function, you're actually passing a reference to that object. This means that the function can modify the object itself.
Immutable objects behave like pass by value:
If you pass an immutable object (like a string, integer, or tuple) to a function, any changes made to the object within the function won't affect the original object outside the function. This is because modifications to immutable objects create new objects.

### Defining Variables
```python
n = 1
n, m = 1, 2
n, m = 1, 'abc'
n = None
```

### Incrementing
```python
n = n + 1
n += 1
```

### If Statements
```python
n = 1
if n == 1:
    something()
elif n == 2:
    something()
else:
    someething()
```

### While Loops
```python
n = 1
while n > 5:
    something()
```

### For Loops
```python
# Range is exclusive
for i in range(5):
    print(i) # 0 1 2 3 4

# From, to, increment (inclusive, exclusive)
for i in range(5, 1, -1):
    print(i) # 5 4 3 2
```
 
## Arithmetic

### Division
```python
5/2 # python uses decimal division by default, = 2.5
5//2 # round down, = 2
3//2 # negative numbers round down, = -2
```

### Modulo
```python
10 % 3 # = 1

# Negative modulo
-1 % 3 # this is different than other languages, = 2
```

### Math Import
```python
# Round down
math.floor(3/2)

# Round up
math.ceil(3/2)

# Square Root
math.sqrt(2)

# Power
math.pow(3, 2) # base, exponent
```

### Infinity
```python
float("inf")
float("-inf")
```

## Lists
Lists are dynamic in python by default. You can use them as a stack.
```python
# Initialize an list
arr = [1, 2, 3]

# Add element to end of list
arr.append(4)

# Remove last element
arr.pop() # returns the value

# Insert element at index
arr.insert(1, 7) # index, element (O(n) time

# Get element at index
arr[0] = 0

# Initialize list with elements and size
arr = [1] * 5

# Get lenght of list
len(arr)

# Negative list index
arr[-1] # -1 is the last  value

# Sublist
arr[1:3] # inclusive, exclusive

# Unpacking
a, b, c = [1, 2, 3] # useful for going through list of pairs, number of variables must equal length of list

# Iterate through list
for n in arr:
    print(n)

# Iterate through list with index
for i, n in enumerate(arr):
    print(i, n) # i is index, n is value

# Iterate through multiple lists at same time
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2) # combines elements at same index, this prints 1 2, 3 4, etc.

# Reverse
arr.reverse()

# Sort
arr.sort() # ascending by default
arr.sort(reverse = True)

# Custom sort
arr.sort(key=lambda x: len(x)) # sorts by length, ascending order

# List comprehension
arr = [i for i in range(5)] # [0, 1, 2, 3, 4]
arr = [i+i for i in range(5)] # [0, 2, 4, 6, 8]
arr = [[0] * 4 for i in range(4)] # 2d list, 4x4 of 0s
arr = [[0] * 4] * 4 # this does NOT work, the 4 lists are the same object if you change one you change all of them
```

## Strings
Strings behave like lists but they are immutable. Anytime you modify a string it creates a new string with is O(n).
```python
s = 'abc'
s[0] = a # this does not work

# Update string
s += 'def' # s = 'abcdef'

# String to int
i = int("123")

# Int to string
s = str(123)

# Ascii value of a character
asc = ord('a')

# Join
strings = ['ab', 'cd', 'ef']
s = "".join(strings) # s = 'abcdef'
s = " ".join(strings) # s = 'ab cd ef'

# Strip
s.strip() # removes whitespaces from beginning and end
s.strip('><') # removes all > and < from beginning and end

# Is Digit
s.isdigit() # returns true if the string only contains digits
```

## Queues (double ended queue)
Queues in python are double ended by default, meaning you can push/pop from the start or end. Under the hood they are doubly linked lists.
```python
from collections import deque

# Initialize queue
queue = deque() 

# Append to right 
queue.append(1)

# Append to left
queue.appendleft(1)

# Pop from left
queue.popleft()

# Pop from right
queue.pop()
```

## HashSet
You can search, remove, and insert elements in constant time, but there cannot be any duplicates. Under the hood it is a hash table, where the values of the set are stored as keys into the hash table. The actual value associated with the key does not matter; as a set we only check if the key exists. If there are collisions, python uses open address probing (usually linear probing).
```python
mySet = set()

# Add element
mySet.add(1)

# Length of set
len(mySet)

# Search element
v = 1 in mySet # true
v = 2 in mySet # false

# Remove element
mySet.remove(1)

# Initialize with a list
mySet = set([1, 2, 3])

# Initialize with set comprehension
mySet = { i for i in range(5) }
```

## HashMap (Dictionary)
You can search, remove, and insert elements in constant time. Under the hood it is a hash table. If there are collisions, python uses open address probing (usually linear probing).
```python
# Initialize hash map
myMap = {}

# Initialize hash map with elements
myMap = { "key1": 1, "key2": 2}

# Add element with key
myMap["alice"] = 8

# Number of keys
len(myMap)

# Get if key exists in map (constant time)
v = "alice" in myMap

# Remove key and value from map
myMap.pop("alice")

# Dict comprehension
myMap = {i: 2*i for in range(3)} # {0: 0, 1: 2, 2: 3}

# Iterate through keys
for key in myMap:
    something()

# Iterate through values
for value in myMap.values():
    something()

# Unpack
for key, val in myMap.items():
    something()
```

## Tuples
Tuples are like arrays but are immutable. These can be used as keys in HashMaps or HashSets. You use this becuase lists cannot be used as keys.
```python
# Initialize
tup = (1, 2, 3)

# Index
tup[1]
```

## Heaps
Heaps are useful for finding the min/max of a list. By default in python heaps are minheaps (0th index is the min). To use a max heap, invert the elements before adding them to the heap. Under the hood in python they are flat lists (which represent a binary tree). For an element i in the list, parent = (i - 1) // 2, left child = 2\*i + 1, right child = 2*i + 2.
```python
import heapq

# Initialize
minHeap = [] # under the hood it is just an array

# Add element
heapq.heappush(minHeap, 3)

# Pop element
heapq.heappop(minHeap) # removes and returns the min element

# Convert array to a heap
arr = [1, 45, 2, 5]
heapq.heapify(arr)
```

## Functions
```python
def myFunc(param1, param2):
    n = 1
    return

# Modify but not reassign variables unless using nonlocal keyword
def double(arr, val):
    def helper():
        # Modifying array works
        for i, n in enumerate(arr):
            arr[i] *= 2 # modifies original array

        # Will only modify val in helper scope
        val *= 2

        # Need nonlocal to modify outside scope
        nonlocal val
        val *= 2
```

## Classes
```python
class MyClass:
    # Constructor
    def __init__(self, nums):
        # Member variables
        self.nums = nums
    
    # Less than comparator
    def __lt__(self, other):
        return self.nums < other.nums
    
    def __repr__(self):
        return f"Nums: {self.nums}"
```