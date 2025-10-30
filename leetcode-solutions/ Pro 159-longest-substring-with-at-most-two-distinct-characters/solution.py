# Leetcode  Pro 159:  Longest Substring with At Most Two Distinct Characters
# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

class Solution:
    """
    LeetCode 159: Longest Substring with At Most Two Distinct Characters
    Three methods included:
    1. Sliding window using dict (O(n) time, O(n) space)
    2. Brute force with set (O(n^2) time, O(1) space)
    3. Sliding window using Counter (O(n) time, O(n) space)
    """

    # Method 1: Sliding window using dict
    def lengthOfLongestSubstringTwoDistinct_dict(self, s: str) -> int:
        if len(set(s)) <= 2:
            return len(s)

        left = 0
        max_length = 0
        seen = {}

        for i, ch in enumerate(s):
            seen[ch] = seen.get(ch, 0) + 1

            while len(seen) > 2:
                seen[s[left]] -= 1
                if seen[s[left]] == 0:
                    del seen[s[left]]
                left += 1

            max_length = max(max_length, i - left + 1)

        return max_length

    # Method 2: Brute force using set
    def lengthOfLongestSubstringTwoDistinct_brute(self, s: str) -> int:
        if len(set(s)) <= 2:
            return len(s)

        max_length = 0
        for start in range(len(s)):
            seen = set()
            for end in range(start, len(s)):
                seen.add(s[end])
                if len(seen) > 2:
                    break
                max_length = max(max_length, end - start + 1)

        return max_length

    # Method 3: Sliding window using Counter
    def lengthOfLongestSubstringTwoDistinct_counter(self, s: str) -> int:
        if len(set(s)) <= 2:
            return len(s)

        left = 0
        max_length = 0
        char_count = Counter()

        for right, ch in enumerate(s):
            char_count[ch] += 1

            while len(char_count) > 2:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
