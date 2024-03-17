#https://leetcode.com/problems/largest-substring-between-two-equal-characters/description/

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        return(max([s.rfind(i) - s.find(i) - 1 for i in s]))
