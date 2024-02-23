class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        length = 0
        l = 0
    
        for i in range(len(s)):
            while s[i] in substring:
                substring.remove(s[l])
                l += 1
            substring.add(s[i])
            length = max(length, i - l + 1)

        return(length)
