# Leetcode pro 3571 - Shortest Superstring

[🔗 Problem Link](https://leetcode.com/problems/shortest-superstring/)

## Description

You are given two strings, s1 and s2. Return the shortest possible string that contains both s1 and s2 as substrings. If there are multiple valid answers, return any one of them.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s1 = "aba", s2 = "bab"

Output: "abab"

Explanation:

"abab" is the shortest string that contains both "aba" and "bab" as substrings.

Example 2:

Input: s1 = "aa", s2 = "aaa"

Output: "aaa"

Explanation:

"aa" is already contained within "aaa", so the shortest superstring is "aaa".

Constraints:

1 <= s1.length <= 100
1 <= s2.length <= 100
s1 and s2 consist of lowercase English letters only.

## Complexity

Time Complexity: O(n^2)
Space Complexity: O(n)

## Solution

See [`solution.py`](solution.py)
