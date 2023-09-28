from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        result = []
        if strs[0] == None:
            return None
        elif len(strs) == 1:
            return strs[0]
        for i in range(len(strs)):
            j = i + 1
            while j < len(strs):
                if sorted(strs[i]) == sorted(strs[j]):
                    hashmap[i,j - 1] = strs[j]
                #else:
                 #   hashmap[i] = strs[i]
                  #  break
                j += 1
        return hashmap
solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))