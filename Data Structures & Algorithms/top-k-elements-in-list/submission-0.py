class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        # [
        # [],
        # [],
        # [],
        # [],
        # [],
        # [],
        # []
        # ]


        for n in nums:
            count[n] = 1 +count.get(n,0)


        #[99,1,1,2,2,3,3,3,3]
            # n:c
            # key:value(qty)
            # 99  |   1
            # 1   |   2
            # 2   |   2
            # 3   |   4



        for n,c in count.items():
            freq[c].append(n)

            #   c:n
            #index:value
            # 1   |  [ 99]
            # 2   |  [ 1,  2]
            # 4   |   [3]

        res = []
        for i in range(len(freq) -1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k: # stops when k is equal to res lenght
                    return res

