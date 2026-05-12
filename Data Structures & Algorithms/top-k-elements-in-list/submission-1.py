class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d2=sorted(Counter(nums).items(),key=lambda x: -x[1])
        return [num for num,_ in d2[:k]]