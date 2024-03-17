#https://leetcode.com/problems/richest-customer-wealth/description/

class Solution(object):
    def maximumWealth(self, accounts):
        summ = []
        for i in accounts:
            summ.append(sum(i))
        return max(summ)
