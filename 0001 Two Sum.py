class Solution(object):
    def twosum(self, nums, target):
        diff_dict = {}
        for i, num in enumerate(nums):
            if num in diff_dict:
                return [diff_dict[num], i]
            else:
                diff_dict[target - num] = i