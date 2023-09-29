from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = nums
        i = 0
        while i < len(answer):
            j = i + 1
            while j < len(answer):
                nums[i] *= answer[j - 1]
                j += 1
                
            i += 1
        return nums
solution = Solution()
print(solution.productExceptSelf([1,2,3,4]))