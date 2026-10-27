# 455. Assign Cookies

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-Two_Pointers-blue) ![Topic](https://img.shields.io/badge/Topic-Greedy-blue) ![Topic](https://img.shields.io/badge/Topic-Sorting-blue) ![Topic](https://img.shields.io/badge/Topic-Quicksort-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 23 ms |
| Memory | 21.9 MB |
| Submission Date | 2026-10-27T12:36:31.045Z |
| Platform | leetcode |

## Problem Statement

<p>Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.</p>

<p>Each child <code>i</code> has a greed factor <code>g[i]</code>, which is the minimum size of a cookie that the child will be content with; and each cookie <code>j</code> has a size <code>s[j]</code>. If <code>s[j] &gt;= g[i]</code>, we can assign the cookie <code>j</code> to the child <code>i</code>, and the child <code>i</code> will be content. Your goal is to maximize the number of your content children and output the maximum number.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> g = [1,2,3], s = [1,1]
<strong>Output:</strong> 1
<strong>Explanation:</strong> You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> g = [1,2], s = [1,2,3]
<strong>Output:</strong> 2
<strong>Explanation:</strong> You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children, 
You need to output 2.
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= g.length &lt;= 3 * 10<sup>4</sup></code>
- <code>0 &lt;= s.length &lt;= 3 * 10<sup>4</sup></code>
- <code>1 &lt;= g[i], s[j] &lt;= 2<sup>31</sup> - 1</code>

## Solution

```py
class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()

        child = 0
        cookie = 0

        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                child += 1
            cookie += 1

        return child 
```

[View on LeetCode](https://leetcode.com/problems/assign-cookies/)
