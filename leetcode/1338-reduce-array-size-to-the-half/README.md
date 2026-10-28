# 1338. Reduce Array Size to The Half

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Hash_Table-blue) ![Topic](https://img.shields.io/badge/Topic-Greedy-blue) ![Topic](https://img.shields.io/badge/Topic-Sorting-blue) ![Topic](https://img.shields.io/badge/Topic-Heap_(Priority_Queue)-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 154 ms |
| Memory | 42.5 MB |
| Submission Date | 2026-10-28T06:05:27.159Z |
| Platform | leetcode |

## Problem Statement

<p>You are given an integer array <code>arr</code>. You can choose a set of integers and remove all the occurrences of these integers in the array.</p>

<p>Return <em>the minimum size of the set so that <strong>at least</strong> half of the integers of the array are removed</em>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> arr = [3,3,3,3,5,5,5,2,2,7]
<strong>Output:</strong> 2
<strong>Explanation:</strong> Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half of the size of the old array.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> arr = [7,7,7,7,7,7]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The only possible set you can choose is {7}. This will make the new array empty.
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>2 &lt;= arr.length &lt;= 10<sup>5</sup></code>
- <code>arr.length</code> is even.
- <code>1 &lt;= arr[i] &lt;= 10<sup>5</sup></code>

## Solution

```py
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

```

[View on LeetCode](https://leetcode.com/problems/reduce-array-size-to-the-half/)
