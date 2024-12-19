# 1456. Maximum Number of Vowels in a Substring of Given Length
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/?envType=study-plan-v2&envId=leetcode-75

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

### Example 1:

```
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
```

### Example 2:

```
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
```

### Example 3:

```
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
```

### Constraints:

```
1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length
```

### Solution:

```python
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        
        m = cur = 0
        
        # Calculate first window
        for i in range(0, k):
            if s[i] in vowels:
                m += 1
                cur += 1

        # Iterate through each index after initial window until end
        for i in range(k, len(s)):
            # If newest addition is a vowel and end of last window is not a vowel
            # We are gaining a vowel and losing a consonant so add to the current
            if s[i] in vowels and s[i-k] not in vowels:
                cur += 1
            # If newest addition is not a vowel and end of last window was a vowel
            # We are losing a vowel and gaining a consonant so sub from the current
            if s[i] not in vowels and s[i-k] in vowels:
                cur -= 1
            
            # Get the max of this wondow or the maximum
            m = max(m, cur)
        return m
```