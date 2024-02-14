#https://leetcode.com/problems/merge-similar-items/
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        sums_dict = {}
        for sublist in items1 + items2:
            key = sublist[0]
            value = sublist[1]
            if key in sums_dict:
                sums_dict[key] += value
            else:
                sums_dict[key] = value
        ret = [[key, value] for key, value in sums_dict.items()]
        return(sorted(ret))