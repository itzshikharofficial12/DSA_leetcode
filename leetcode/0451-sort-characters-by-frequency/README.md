# 451. Sort Characters By Frequency

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Hash_Table-blue) ![Topic](https://img.shields.io/badge/Topic-String-blue) ![Topic](https://img.shields.io/badge/Topic-Sorting-blue) ![Topic](https://img.shields.io/badge/Topic-Heap_(Priority_Queue)-blue) ![Topic](https://img.shields.io/badge/Topic-Bucket_Sort-blue) ![Topic](https://img.shields.io/badge/Topic-Counting-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 11 ms |
| Memory | 19.9 MB |
| Submission Date | 2026-10-28T05:27:53.672Z |
| Platform | leetcode |

## Problem Statement

<p>Given a string <code>s</code>, sort it in <strong>decreasing order</strong> based on the <strong>frequency</strong> of the characters. The <strong>frequency</strong> of a character is the number of times it appears in the string.</p>

<p>Return <em>the sorted string</em>. If there are multiple answers, return <em>any of them</em>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> s = &quot;tree&quot;
<strong>Output:</strong> &quot;eert&quot;
<strong>Explanation:</strong> &#39;e&#39; appears twice while &#39;r&#39; and &#39;t&#39; both appear once.
So &#39;e&#39; must appear before both &#39;r&#39; and &#39;t&#39;. Therefore &quot;eetr&quot; is also a valid answer.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> s = &quot;cccaaa&quot;
<strong>Output:</strong> &quot;aaaccc&quot;
<strong>Explanation:</strong> Both &#39;c&#39; and &#39;a&#39; appear three times, so both &quot;cccaaa&quot; and &quot;aaaccc&quot; are valid answers.
Note that &quot;cacaca&quot; is incorrect, as the same characters must be together.
</pre>

<p>
```

**Example 3:**

```
</p>

<pre>
<strong>Input:</strong> s = &quot;Aabb&quot;
<strong>Output:</strong> &quot;bbAa&quot;
<strong>Explanation:</strong> &quot;bbaA&quot; is also a valid answer, but &quot;Aabb&quot; is incorrect.
Note that &#39;A&#39; and &#39;a&#39; are treated as two different characters.
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= s.length &lt;= 5 * 10<sup>5</sup></code>
- <code>s</code> consists of uppercase and lowercase English letters and digits.

## Solution

```py
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
```

[View on LeetCode](https://leetcode.com/problems/sort-characters-by-frequency/)
