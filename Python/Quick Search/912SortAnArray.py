class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
            
        pivot = random.choice(nums)
        less = [num for num in nums if num < pivot]
        greater = [num for num in nums if num > pivot]
        equal = [pivot] * (len(nums) - len(greater) - len(less))

        return self.sortArray(less) + equal + self.sortArray(greater)



# Previous attempt which exceeded time limit
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums) - 1)
        return nums

    def quicksort(self, arr, low, high):
        if low < high:
            pivot = self.partition(arr, low, high)

            self.quicksort(arr, low, pivot - 1)
            self.quicksort(arr, pivot + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low

        for j in range(low, high):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i], arr[high] = arr[high], arr[i]
        return i

        
        
