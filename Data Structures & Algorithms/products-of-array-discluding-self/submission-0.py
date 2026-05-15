class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)

        pf=[None]*n
        pf[0]=1
        for i in range(1,n):
            pf[i]=nums[i-1]*pf[i-1]

        sf=[None]*n
        sf[n-1]=1
        for i in range(n-2,-1,-1):
            sf[i]=nums[i+1]*sf[i+1]

        res=[None]*n
        for i in range(n):
            res[i]=pf[i]*sf[i]

        return res
                 

