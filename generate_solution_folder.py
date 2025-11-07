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
        f.write("## Description\n\n Time Complexity: O(n)\nSpace Complexity: O(n) \n\n")
        f.write("## Solution\n\nSee [`solution.py`](solution.py)\n")

    print(f"[✅] Created folder and files at: {base_path}")

if __name__ == "__main__":
    problem_number = " pro 3641"
    problem_title = " Longest Semi-Repeating Subarray"
    solution_code = '''
from collections import Counter
class Solution:
    def fre(self, nums: list[int], k: int) -> int:
        maxx=left= rep=0
        count=Counter()
        for right in range(len(nums)):
            count[nums[right]]+=1
            if count[nums[right]]==2:
                rep+=1
            while rep>k:
                if count[nums[left]]==2:
                    rep-=1
                count[nums[left]]-=1
                left+=1
            maxx=max(maxx, right-left+1)
        return maxx
'''
    create_leetcode_problem_folder(problem_number, problem_title, solution_code)
