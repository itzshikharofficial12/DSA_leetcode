# 57. Insert Interval

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 0 ms |
| Memory | 21.5 MB |
| Submission Date | 2026-10-29T05:48:41.830Z |
| Platform | leetcode |

## Problem Statement

<p>You are given an array of non-overlapping intervals <code>intervals</code> where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code> represent the start and the end of the <code>i<sup>th</sup></code> interval and <code>intervals</code> is sorted in ascending order by <code>start<sub>i</sub></code>. You are also given an interval <code>newInterval = [start, end]</code> that represents the start and end of another interval.</p>

<p>Two intervals are considered overlapping if they share <strong>at least</strong> one point.</p>

<p>Insert <code>newInterval</code> into <code>intervals</code> such that <code>intervals</code> is still sorted in ascending order by <code>start<sub>i</sub></code> and <code>intervals</code> still does not have any overlapping intervals (merge overlapping intervals if necessary).</p>

<p>Return <code>intervals</code><em> after the insertion</em>.</p>

<p><strong>Note</strong> that you don&#39;t need to modify <code>intervals</code> in-place. You can make a new array and return it.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> intervals = [[1,3],[6,9]], newInterval = [2,5]
<strong>Output:</strong> [[1,5],[6,9]]
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
<strong>Output:</strong> [[1,2],[3,10],[12,16]]
<strong>Explanation:</strong> Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>0 &lt;= intervals.length &lt;= 10<sup>4</sup></code>
- <code>intervals[i].length == 2</code>
- <code>0 &lt;= start<sub>i</sub> &lt;= end<sub>i</sub> &lt;= 10<sup>5</sup></code>
- <code>intervals</code> is sorted by <code>start<sub>i</sub></code> in <strong>ascending</strong> order.
- <code>newInterval.length == 2</code>
- <code>0 &lt;= start &lt;= end &lt;= 10<sup>5</sup></code>

## Solution

```py
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        intervals.append(newInterval)
        intervals.sort()
        s = intervals[0][0]
        e = intervals[0][1]
        n = len(intervals)
        v = []

        for i in range(1, n):
            if e >= intervals[i][0]:
                s = min(s, intervals[i][0])
                e = max(e, intervals[i][1])

            else:
                v.append([s,e])
                s = intervals[i][0]
                e = intervals[i][1]

        v.append([s,e])
        return v
```

[View on LeetCode](https://leetcode.com/problems/insert-interval/)
