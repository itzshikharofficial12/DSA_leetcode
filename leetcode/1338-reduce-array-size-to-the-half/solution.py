# Runtime: 154 ms
# Memory: 42.5 MB

class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        freq = {}

        for x in arr:
            freq[x] = freq.get(x,0) + 1
        items = []

        for x in freq:
            items.append((freq[x], x))

        items.sort(reverse = True)
        start = len(arr)
        target = len(arr) // 2
        count = 0
        for x in items:
            start -= x[0]
            count += 1
            if start <= target:
                return count 
