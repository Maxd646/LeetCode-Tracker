# Leetcode pro 3672 - Sum of Weighted Modes in Subarrays

[🔗 Problem Link](https://leetcode.com/problems/sum-of-weighted-modes-in-subarrays/)

## Description

Description
You are given an integer array nums and an integer k.

For every subarray of length k:

The mode is defined as the element with the highest frequency. If there are multiple choices for a mode, the smallest such element is taken.
The weight is defined as mode \* frequency(mode).
Return the sum of the weights of all subarrays of length k.

Note:

A subarray is a contiguous non-empty sequence of elements within an array.
The frequency of an element x is the number of times it occurs in the array.

Example 1:

Input: nums = [1,2,2,3], k = 3

Output: 8

Explanation:

Subarrays of length k = 3 are:

Subarray Frequencies Mode Mode
​​​​​​​Frequency Weight
[1, 2, 2] 1: 1, 2: 2 2 2 2 × 2 = 4
[2, 2, 3] 2: 2, 3: 1 2 2 2 × 2 = 4
Thus, the sum of weights is 4 + 4 = 8.

Example 2:

Input: nums = [1,2,1,2], k = 2

Output: 3

Explanation:

Subarrays of length k = 2 are:

Subarray Frequencies Mode Mode
Frequency Weight
[1, 2] 1: 1, 2: 1 1 1 1 × 1 = 1
[2, 1] 2: 1, 1: 1 1 1 1 × 1 = 1
[1, 2] 1: 1, 2: 1 1 1 1 × 1 = 1
Thus, the sum of weights is 1 + 1 + 1 = 3.

Example 3:

Input: nums = [4,3,4,3], k = 3

Output: 14

Explanation:

Subarrays of length k = 3 are:

Subarray Frequencies Mode Mode
Frequency Weight
[4, 3, 4] 4: 2, 3: 1 4 2 2 × 4 = 8
[3, 4, 3] 3: 2, 4: 1 3 2 2 × 3 = 6
Thus, the sum of weights is 8 + 6 = 14.

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
1 <= k <= nums.length

## Complexity

Time Complexity: O(n\*k)
Space Complexity: O(k)

## Solution

See [`solution.py`](solution.py)
