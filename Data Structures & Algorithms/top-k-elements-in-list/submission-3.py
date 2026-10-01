import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dic = defaultdict(int)
        heap = []

        for i in nums: 
            dic[i] += 1 
        for j in dic.keys():
            heapq.heappush(heap, (dic[j], j))
            if len(heap) > k: 
                heapq.heappop(heap)
        return [v for k, v in heap]

