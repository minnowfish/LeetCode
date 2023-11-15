class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedToAnagrams = {}
        for i in strs:
            word = ''.join(sorted(i))
        
            if word not in sortedToAnagrams:
                sortedToAnagrams[word] = [i]
            else:
                sortedToAnagrams[word].append(i)
            
        return sortedToAnagrams.values()
