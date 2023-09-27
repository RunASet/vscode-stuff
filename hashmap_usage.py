from typing import List
from collections import defaultdict
"""
The following is an example of using a hashmap to solve for the group anagram problem.

Pay attention to the usage of the methods, tuple(), append(), values() and defultdict().

We use these special functions to allow us to easily sort this.

Tuple(), is used so we can have multiple elements of our original array assigned to one index
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        result = []
        for s in strs:
            sorted_S = tuple(sorted(s))
            hashmap[sorted_S].append(s)
        for value in hashmap.values():
            result.append(value)
        return result
solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))