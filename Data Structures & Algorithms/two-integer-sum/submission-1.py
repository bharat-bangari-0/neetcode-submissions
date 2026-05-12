class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dc={}
        for ix, val in enumerate(nums):
            rem=target-val
            if rem in dc:
                return [dc[rem],ix]
            dc[val]=ix
        # n=len(nums)
        # for i in range(n-1):
        #     for j in range(i+1,n):
        #         if nums[j]==target-nums[i]:
        #             return [i,j]
        