class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}                          # label -> list of words
        for s in strs:
            key = "".join(sorted(s))
            if key not in groups:            # first word with this label
                groups[key] = []            # start an empty group
            groups[key].append(s)
        return list(groups.values())