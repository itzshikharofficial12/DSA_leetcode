# 14. Longest Common Prefix

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Array-blue) ![Topic](https://img.shields.io/badge/Topic-String-blue) ![Topic](https://img.shields.io/badge/Topic-Trie-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 0 ms |
| Memory | 19 MB |
| Submission Date | 2026-10-19T07:53:51.376Z |
| Platform | leetcode |

## Problem Statement

<p>Write a function to find the longest common prefix string amongst an array of strings.</p>

<p>If there is no common prefix, return an empty string <code>&quot;&quot;</code>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> strs = [&quot;flower&quot;,&quot;flow&quot;,&quot;flight&quot;]
<strong>Output:</strong> &quot;fl&quot;
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> strs = [&quot;dog&quot;,&quot;racecar&quot;,&quot;car&quot;]
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong> There is no common prefix among the input strings.
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= strs.length &lt;= 200</code>
- <code>0 &lt;= strs[i].length &lt;= 200</code>
- <code>strs[i]</code> consists of only lowercase English letters if it is non-empty.

## Solution

```py
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]
        pref_len = len(pref)

        for s in strs[1:]:
            while pref != s[0:pref_len]:
                pref_len -= 1
                if pref_len == 0:
                    return ""
                
                pref = pref[0:pref_len]
        
        return pref
```

[View on LeetCode](https://leetcode.com/problems/longest-common-prefix/)
