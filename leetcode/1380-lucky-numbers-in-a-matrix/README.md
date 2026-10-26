# 1380. Lucky Numbers in a Matrix

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Matrix-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 2 ms |
| Memory | 19.7 MB |
| Submission Date | 2026-10-26T13:00:01.446Z |
| Platform | leetcode |

## Problem Statement

<p>Given an <code>m x n</code> matrix of <strong>distinct </strong>numbers, return <em>all <strong>lucky numbers</strong> in the matrix in <strong>any </strong>order</em>.</p>

<p>A <strong>lucky number</strong> is an element of the matrix such that it is the minimum element in its row and maximum in its column.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> matrix = [[3,7,8],[9,11,13],[15,16,17]]
<strong>Output:</strong> [15]
<strong>Explanation:</strong> 15 is the only lucky number since it is the minimum in its row and the maximum in its column.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
<strong>Output:</strong> [12]
<strong>Explanation:</strong> 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
</pre>

<p>
```

**Example 3:**

```
</p>

<pre>
<strong>Input:</strong> matrix = [[7,8],[1,2]]
<strong>Output:</strong> [7]
<strong>Explanation:</strong> 7 is the only lucky number since it is the minimum in its row and the maximum in its column.
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>m == mat.length</code>
- <code>n == mat[i].length</code>
- <code>1 &lt;= n, m &lt;= 50</code>
- <code>1 &lt;= matrix[i][j] &lt;= 10<sup>5</sup></code>.
- All elements in the matrix are distinct.

## Solution

```py
class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        row_mins = {min(row) for row in matrix}

        col_maxs = {max(col) for col in zip(*matrix)}
        
        return list(row_mins.intersection(col_maxs))
```

[View on LeetCode](https://leetcode.com/problems/lucky-numbers-in-a-matrix/)
