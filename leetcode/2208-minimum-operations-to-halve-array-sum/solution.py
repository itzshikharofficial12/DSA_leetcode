# Runtime: 260 ms
# Memory: 32.8 MB

class Solution:
    def halveArray(self, nums: list[int]) -> int:
        max_heap = [-x for x in nums]
        heapify(max_heap)
        start = sum(nums)
        target_sum = start/2
        count = 0
        while start > target_sum:
            maxi = -heappop(max_heap) 
            start -= maxi/2
            heappush(max_heap, -maxi/2)
            count += 1

        return count 