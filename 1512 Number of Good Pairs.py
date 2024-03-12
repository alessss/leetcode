#https://leetcode.com/problems/number-of-good-pairs/

class Solution(object):
    def numIdenticalPairs(self, nums):
        nnums = []
        res = 0
        for i in nums:
            if i not in nnums: 
                count = nums.count(i)
                res += (count*(count-1)//2)
                nnums.append(i)
        return res
