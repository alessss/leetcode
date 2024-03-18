#https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return(set([chr(x) for x in range (97, 123)]) == set(sentence))
