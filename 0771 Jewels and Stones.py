#https://leetcode.com/problems/jewels-and-stones/
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        sum = 0
        for i in jewels:
            sum += stones.count(i)
        return sum
