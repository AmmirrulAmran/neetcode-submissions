class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mainList = []
        used = set()
        for i in range(len(strs)):
            temp = []
            if strs[i] in used:
                continue
            else: 
                used.add(strs[i])
                temp.append(strs[i])

                for j in range(i+1, len(strs)):
                    
                    if sorted(strs[i]) == sorted(strs[j]):
                        temp.append(strs[j])
                        used.add(strs[j])

                    
                mainList.append(temp)



        return mainList
                    