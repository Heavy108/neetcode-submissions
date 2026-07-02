class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
       

        for i in range(0,len(nums)):
            if nums[i] in res:
                res[nums[i]] += 1
            else:
                res[nums[i]] = 1

        # for n,c in res.items():
        #     freq[c].append(n)
        # ans =[]
        # for i in range(len(freq)-1,0,-1):
        #     for n in freq[i]:
        #         ans.append(n)
        #         if len(ans)==k:
        #             return ans

        sorted_items =sorted(res.items() ,key=lambda x:x[1] ,reverse=True)

        return [key for key,value in sorted_items[:k]]
        
        
        
        