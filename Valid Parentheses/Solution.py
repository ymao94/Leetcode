class Solution:
    def isValid(self, s: str) -> bool:
        left = ['(','{','[']
        mapping = {'(':')','{':'}','[':']'}
        stack = []
        for i in s:
            if i in left:
                stack.append(i)
            else:
                if stack and mapping[stack[-1]] == i:
                #attention! hier ist das Kommando "if stack" wichtig, weil sonst
                # wenn der Stack leer ist und trotzdem ein )}] getroffen hat,
                # taucht ein Fehler auf
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False
        
        
        
