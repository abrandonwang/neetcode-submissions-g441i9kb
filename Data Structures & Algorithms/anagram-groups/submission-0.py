class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collection = {}
        # "eat": ["eat", "tea", "ate"], "atn": ["tan", "nat"] ... 
        for string in strs:
            key = "".join(sorted(string))
            if key in collection:
                collection[key].append(string)
            else:
                collection[key] = [string]
        return list(collection.values())