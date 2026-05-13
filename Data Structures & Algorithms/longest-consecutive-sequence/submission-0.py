class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett=set(nums)
        mx=0
        for num in sett:
            if num-1 not in sett:
                l=1
                curr=num
                while curr+1 in sett:
                    curr+=1
                    l+=1
                mx=max(mx,l)
        return mx
        