# Leetcode 3333: Find the Original Typed String II
# https://leetcode.com/problems/find-the-original-typed-string-ii/

class Solution:
  def possibleStringCount(self, word: str, k: int) -> int:
    kMod = 1_000_000_007
    words = self._getConsecutiveLetters(word)
    totalCombinations = functools.reduce(lambda subtotal, word:
                                         subtotal * word % kMod, words)
    if k <= len(words):
      return totalCombinations
    dp = [0] * k
    dp[0] = 1  

    for i, word in enumerate(words):
      newDp = [0] * k
      windowSum = 0
      for j in range(i, k):
        newDp[j] = (newDp[j] + windowSum) % kMod
        windowSum = (windowSum + dp[j]) % kMod
        if j >= word:
          windowSum = (windowSum - dp[j - word] + kMod) % kMod
      dp = newDp

    return (totalCombinations - sum(dp)) % kMod

  def _getConsecutiveLetters(self, make: str) -> list[int]:
    words = []
    word = 1
    for i in range(1, len(make)):
      if make[i] == make[i - 1]:
        word += 1
      else:
        words.append(word)
        word= 1
    words.append(word)
    return words
