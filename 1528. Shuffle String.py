#https://leetcode.com/problems/shuffle-string/description/

class Solution(object):
    def restoreString(self, s, indices):
        shuffled = list(' ' * len(s))
        for i,j in zip(s, indices):
            shuffled[j] = i
        return ''.join(map(str, shuffled))
