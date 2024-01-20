class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [1]*length
        pre = 1
        post =1 
        for i in range(len(nums)):
            ans[i] *= pre
            pre *= nums[i]
            ans[length - i - 1] *= post
            post *= nums[length - i - 1]
        return(ans)
