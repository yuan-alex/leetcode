class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = [(val * -1, key) for key, val in collections.Counter(words).items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for i in range(k)]