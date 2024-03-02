#https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/

class Solution(object):
    def countPairs(self, nums, target):
        counter = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] < target:
                    counter+=1
        return(counter)
