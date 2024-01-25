class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = set(nums)
        length = 1
        for i in nums:
            if i - 1 in nums:
                continue
            consec = 1
            while i + 1 in nums:
                consec += 1
                i = i + 1
            length = max(length,consec)
        return length
