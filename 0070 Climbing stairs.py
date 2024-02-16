#https://leetcode.com/problems/climbing-stairs/description/
class Solution:
    def climbStairs(self, n: int) -> int:
        fibArray = [0, 1]
        for i in range(2, n+2):
            fibArray.append(fibArray[i-1] + fibArray[i-2])
        return fibArray[n+1]