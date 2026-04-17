class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # my_dict = {1: 1, 2: 2, 3: 3}
        # loop through k times, checking for max
        my_dict = {}
        for i in nums:
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1
        print(my_dict)
        
        return sorted(my_dict, key = lambda x: my_dict[x], reverse=True)[:k]
