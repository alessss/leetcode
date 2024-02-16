#https://leetcode.com/problems/fibonacci-number/
class Solution(object):
    def fib(self, n):
        fibArray = [0, 1]
        for i in range(2, n+1):
            fibArray.append(fibArray[i-1] + fibArray[i-2])
        return fibArray[n]
