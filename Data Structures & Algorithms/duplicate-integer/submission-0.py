class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d=Counter(nums)
        for value in d.values():
            if value>1:
                return True
        return False
        