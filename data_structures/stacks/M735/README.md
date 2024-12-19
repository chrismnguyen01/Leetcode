# 735. Asteroid Collision
https://leetcode.com/problems/asteroid-collision/?envType=study-plan-v2&envId=leetcode-75

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

### Example 1:

```
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
```

### Example 2:

```
Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
```

### Example 3:

```
Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
```

### Constraints:

```
2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
```

```python
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in asteroids:
            # while there are asteroids in the stack and we have a negative asteroid
            while stack and stack[-1] > 0 and i < 0:
                # if the negative asteroid is bigger than the last positive one then remove it
                if i + stack[-1] < 0:
                    stack.pop()
                # if they are equal then remove it and get to the next asteroid
                elif i == -stack[-1] or -i == stack[-1]:
                    stack.pop()
                    break
                else:
                    break
            # if we have a positive asteroid add it to the stack
            # this is while else loop it will only execute if we don't go into the while loop
            else:
                stack.append(i)

        
        return stack
```