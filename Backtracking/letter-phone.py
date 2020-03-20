""" Phone Letter Backtracking Problem,
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



The digit 0 maps to 0 itself.
The digit 1 maps to 1 itself.

Input: Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]. 

"""

def letterCombinations(self, digits):
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz', '0': '0', '1': '1'}
        result = []
        possible = ""
        index = 0
        n = len(digits)
        def helper(mapping, index, possible,result):
            if len(possible)== n:
                result.append(possible)
                return
            else:
                for letter in mapping[digits[index]]:
                    possible+=letter
                    helper(mapping,index+1,possible,result)
                    #backtracking
                    possible = possible[:-1]
        helper(mapping, index, possible, result)
        return result
