# 151. Reverse Words in a String
https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

### Example 1:

```
Input: s = "the sky is blue"
Output: "blue is sky the"
```

### Example 2:

```
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
```

### Example 3:

```
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
```

### Constraints:

```
1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
```

## Code

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Reverse the entire string
        s = list(s)
        s.reverse()

        # Step 2: Reverse each word in the string and handle spaces
        start = 0
        n = len(s)
        words = []

        for i in range(n):
            if s[i] == ' ' or i == n - 1:
                # If we reach a space or the end of the string
                end = i if s[i] == ' ' else i + 1  # Consider the end of the last word
                if start < end:
                    self.reverse_word(s, start, end - 1)
                    words.append(''.join(s[start:end]))  # Add reversed word to the result
                start = i + 1

        # Step 3: Join words with a single space and return
        return ' '.join(words)

    def reverse_word(self, s, start, end):
        # Helper function to reverse a word in place
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
```