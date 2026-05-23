class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # mainList = []
        # used = set()
        # for i in range(len(strs)):
        #     temp = []
        #     if strs[i] in used:
        #         continue
        #     else: 
        #         used.add(strs[i])
        #         temp.append(strs[i])

        #         for j in range(i+1, len(strs)):
                    
        #             if sorted(strs[i]) == sorted(strs[j]):
        #                 temp.append(strs[j])
        #                 used.add(strs[j])

                    
        #         mainList.append(temp)



        # return mainList



        from collections import defaultdict

        res = defaultdict(list) #create a dict with default of empty list

        for s in strs:
            count = [0]*26

            for c in s:
                count[ord(c) - ord("a")] +=1

            res[tuple(count)].append(s)

        return list(res.values())








                    