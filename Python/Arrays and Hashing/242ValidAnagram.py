class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charToFreq = {}
        for char in s:
            charToFreq[char] = charToFreq.get(char, 0) +1
        
        for char in t:
            if char not in charToFreq or charToFreq[char] == 0:
                return False
            else:
                charToFreq[char] -= 1
        return True
        
