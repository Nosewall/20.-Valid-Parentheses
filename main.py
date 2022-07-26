class Solution:
    def isValid(self, s: str):
        #Initialize array to track progress through the stack
        stack = []
        #All possible opening brackets
        leftParenthesis = '({['

        pairdict = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for parenthesis in s:
            if parenthesis in leftParenthesis:
                stack.append(pairdict[parenthesis])
            #Checks to see if there is a right parentheses, which is a failure
            elif len(stack) == 0:
                return False
            elif parenthesis != stack.pop():
                return False
        return len(stack) == 0
