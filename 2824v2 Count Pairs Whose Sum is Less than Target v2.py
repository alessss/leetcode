# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/submissions/1191086251/

class Solution(object):
    def countPairs(self, nums, target):
        return(len([(nums[x],nums[y]) for x in range(len(nums)-1) for y in range(x+1, len(nums)) if nums[x] + nums[y] < target]))
