class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyToNum = {}
        l = []
        for i in nums:
            if i in frequencyToNum:
                frequencyToNum[i] +=1
            else:
                frequencyToNum[i] = 1

        index = sorted(frequencyToNum.values(),reverse = True)[k-1]
        for i in frequencyToNum:
            if frequencyToNum[i] >= index:
                l.append(i)
        return l
