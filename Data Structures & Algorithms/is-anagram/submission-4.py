
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if sorted(t) != sorted(s):
            return False

        else:
            return True

        if len(t) != len(s):
            return False

        else:

            S, T = {},{}

            for x in range(len(s)):
                S[s[x]] = 1 + S.get(s[x],0)
                T[t[x]] = 1 + T.get(t[x],0)


            for y in S:
                if S[y] != T.get(y,0):
                    return False


        return True

    
