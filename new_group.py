from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs == None:
            return None
        elif len(strs) == 1:
            return strs[0]
        CountS, CountT = {}, {}
solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))