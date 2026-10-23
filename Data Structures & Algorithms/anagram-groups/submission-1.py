class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for n in strs:
            key = "".join(sorted(n))
            group[key].append(n)
        return list(group.values())    