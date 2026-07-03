class Solution:
    def isValid(self, s: str) -> bool: 
        stack=[]
        CloseToOpen ={
            ")":"(",
            "}":"{",
            "]":"["
        }

        for c in s:
            if c not in CloseToOpen:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if popped != CloseToOpen[c]:
                        return False
        return not stack


        