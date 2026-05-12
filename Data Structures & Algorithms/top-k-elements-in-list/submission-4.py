class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d1=Counter(nums)
        d2=sorted(d1.items(),key=lambda x: -x[1])
        return [num for num,_ in d2[:k]]