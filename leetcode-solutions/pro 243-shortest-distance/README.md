# Leetcode pro 243 - Shortest Distance

[🔗 Problem Link](https://leetcode.com/problems/shortest-distance/)

## Description

# 243. Shortest Word Distance

Given an array of strings wordsDict and two different strings word1 and word2, return the shortest distance between these two words in the list.

The words are given in order, and the distance between two indices i and j is the absolute difference |i - j|.

Example 1:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3

Example 2:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1

Constraints:

1 <= wordsDict.length <= 3 \* 10^4
1 <= wordsDict[i].length <= 10
wordsDict[i] consists of lowercase English letters.
word1 and word2 are in wordsDict.
word1 != word2

# Complexity

Time Complexity: O(n)
Space Complexity: O(1)

## Solution

See [`solution.py`](solution.py)
