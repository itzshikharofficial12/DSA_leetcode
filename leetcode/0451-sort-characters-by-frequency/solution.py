# Runtime: 11 ms
# Memory: 19.9 MB

# class Solution:
#     def frequencySort(self, s: str) -> str:
        # def f(ch):
        #     for i in s:
        #         if i == ch:
        #             c += 1

        

# from collections import Counter

# class Solution:
#     def frequencySort(self, s: str) -> str:
#         return "".join(char * freq for char, freq in Counter(s).most_common())

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for i in s:
            freq[i] = freq.get(i, 0) + 1
        j = sorted(freq, key=lambda x: freq[x], reverse=True)
        ans = "" 
        for i in j:
            ans += i * freq[i]
        return ans 