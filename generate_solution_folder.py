import os

def slugify(title):
    return title.strip().lower().replace(" ", "-")

def create_leetcode_problem_folder(problem_number, title, solution_code):
    folder_name = f"{problem_number}-{slugify(title)}"
    base_path = os.path.join("leetcode-solutions", folder_name)
    os.makedirs(base_path, exist_ok=True)

    # Write solution.py
    with open(os.path.join(base_path, "solution.py"), "w", encoding="utf-8") as f:
        f.write(f"# Leetcode {problem_number}: {title}\n")
        f.write(f"# https://leetcode.com/problems/{slugify(title)}/\n\n")
        f.write(solution_code.strip() + "\n")

    # Write README.md
    with open(os.path.join(base_path, "README.md"), "w", encoding="utf-8") as f:
        f.write(f"# Leetcode {problem_number} - {title}\n\n")
        f.write(f"[🔗 Problem Link](https://leetcode.com/problems/{slugify(title)}/)\n\n")
        f.write("## Description\n\n*Add problem description here...*\n\n")
        f.write("## Solution\n\nSee [`solution.py`](solution.py)\n")

    print(f"[✅] Created folder and files at: {base_path}")

if __name__ == "__main__":
    problem_number = 3333
    problem_title = "Find the Original Typed String II"
    solution_code = '''
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
'''

    create_leetcode_problem_folder(problem_number, problem_title, solution_code)
