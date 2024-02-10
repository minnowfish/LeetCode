class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxFrequency = 0
        left = 0

        for i in range(len(s)):
            count[s[i]] = count.get(s[i],0) + 1
            maxFrequency = max(maxFrequency, count[s[i]])

            if (i+1-left) - maxFrequency > k:
                count[s[left]] -= 1
                left += 1
        return(i+1-left)
