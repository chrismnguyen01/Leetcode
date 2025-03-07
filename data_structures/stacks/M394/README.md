# 394. Decode String
https://leetcode.com/problems/decode-string/?envType=study-plan-v2&envId=leetcode-75

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

### Example 1:

```
Input: s = "3[a]2[bc]"
Output: "aaabcbc"
```

### Example 2:

```
Input: s = "3[a2[c]]"
Output: "accaccacc"
```

### Example 3:

```
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
```

### Constraints:

```
1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
```

```python
class Solution:
    def decodeString(self, s):
        stack = []; curNum = 0; curString = ''
        # for each element
        for c in s:
            # if we find a bracket then we add the current running string and number
            # currString goes first because it is not affected by curNum it is only to be
            # popped off and added later
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                # reset current string and number
                curString = ''
                curNum = 0
            # if we find a close bracket we know our curr string needs to be multiplied
            # by last number in the stack and then added to the last string in the stack
            elif c == ']':
                num = stack.pop()
                # prevString is what has been calculated before
                prevString = stack.pop()
                curString = prevString + num*curString
            # if multi digit number add them up
            elif c.isdigit():
                curNum = curNum*10 + int(c)
            # keep adding letters to curString
            else:
                curString += c
        return curString
```