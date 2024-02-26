#https://leetcode.com/problems/defanging-an-ip-address/description/
class Solution(object):
    def defangIPaddr(self, address):
        result = ''
        for i in address:
            if i=='.':
                result += '[.]'
            else:
                result += i
        return result
