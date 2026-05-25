class Solution:

    def encode(self, strs: List[str]) -> str:


        result = ""

        for s in strs:
            result += str(len(s))+'#'+s

        return result

    def decode(self, s: str) -> List[str]:

 #to get the number or delimeter upfront that represents the length of a word

        result = []
        i = 0 # pointer 

        while i < len(s):#goes through the entire encoded string with multiple words
        # 10#wasIaBad??4#code

            j = i

            while s[j] != '#':
                j+=1
            length = int(s[i:j]) #not including j
            #j is at the delimeter
            result.append(s[j+1:j+1+length])
            i = j + 1 + length # goes to next word

        return result
