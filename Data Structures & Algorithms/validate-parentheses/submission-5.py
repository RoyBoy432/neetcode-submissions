class Solution:
    def isValid(self, s: str) -> bool:
        lefts =["{","(","["]; rights = ["}",")","]"]
        corrRL = {"}":"{",")":"(","]":"["}
        x=0
        toclose=list()
        while x < len(s):
            if s[x] in lefts:
                toclose.append(s[x])
                x+=1
            elif s[x] in rights:
                if len(toclose) == 0:
                    return False
                elif corrRL[s[x]] == toclose[-1]:
                    toclose.pop(-1)
                    x+=1
                else:
                    return False
            else:
                return False
        if len(toclose) == 0:
            return True
        else: return False