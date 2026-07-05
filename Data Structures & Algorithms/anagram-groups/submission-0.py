class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)

        for string in strs:

            sorted_key = "".join(sorted(string))

            groups[sorted_key].append(string)
        
        return list(groups.values())
