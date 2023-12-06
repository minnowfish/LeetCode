class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        array = []
        for i in matrix:
            for j in i:
                array.append(j)
        
        l, r = 0, len(array) - 1
        while l <= r:
            mid = l + ((r-l)//2)
            if array[mid] == target:
                return True
            elif array[mid]<target:
                l = mid + 1
            else:
                r = mid - 1
        return(False)
