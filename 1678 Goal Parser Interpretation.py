#https://leetcode.com/problems/goal-parser-interpretation/

class Solution(object):
    def interpret(self, command):
        out = ''
        for cur, next in zip(command, command[1:]):
            if cur == 'G':
                out += 'G'
            elif cur == '(' and next == ')':
                out += 'o'
            elif cur == '(' and next == 'a':
                out += 'al'
        if command[-1] == 'G':
            out += 'G'
        return(out)
