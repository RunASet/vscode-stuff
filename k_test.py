from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        i = 0
        x = []  # array for holding value we need to return I think?
        n = 0
        if len(nums) > 1:
            while i < len(nums):
                j = i + 1
                while j < len(nums):
                    if nums[i] == nums[j]:
                        if x[n] == x[n + 1]: # s*x check for thing
                            break   # exit while loop if a duplicate has been found
                        else:
                            n += 1
                        x[n] = nums[i]
                    else:
                        j += 1
                i +=1
            k = len(x)  # what ?