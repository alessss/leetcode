#https://leetcode.com/problems/minimum-number-game/description/

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        return([item for sublist in [(nums[i + 1], nums[i]) for i in range(0, len(nums) - 1, 2)] for item in sublist])
