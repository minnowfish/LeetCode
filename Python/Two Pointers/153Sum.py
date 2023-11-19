class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triples = []
        length = len(nums)
        if length == 3:
            if  nums[0] + nums[1] + nums[2] == 0:
                 return [[nums[0],nums[1],nums[2]]]
            else:
                 return []
        
        nums.sort()
        for i,a in enumerate(nums):
            if a>0:
                break
            
            if i>0 and a==nums[i-1]:
                continue
            
            j,k = i + 1, length -1
            while j<k:
                total = a + nums[j] + nums[k]
                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1

                else: 
                    triples.append([a, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j-1] and j<k:
                        j += 1

        return(triples)
