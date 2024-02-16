#https://leetcode.com/problems/zigzag-conversion/
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = ["" for x in range(numRows)]
        res = ([n for n in range(0, numRows, 1)] + [j for j in range(numRows - 2, 0, -1)])
        res = res * (len(s) // len(res)) + res[:len(s) % len(res)]
        for i, j in zip(s, res):
            result[j] += i
        res_str = ""
        for x in result:
            res_str += x
        return res_str