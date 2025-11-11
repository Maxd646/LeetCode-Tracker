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
    problem_number = "pro 1133 "
    problem_title = " Largest Unique Number"
    solution_code = '''
class Solution:
    def largestUniqueNumber(self, nums: list[int]) -> int:
        count={}
        for ch in nums:
            if ch in count:
                count[ch]+=1
            else:
                count[ch]=1
        maxx=-float("inf")
        for ch, num in count.items():
            if ch>maxx and num==1:
                maxx=ch
        return maxx if maxx!=-float("inf") else -1
# or 
from collection import Counter
class Solution:
    def largestUniqueNumber(self, nums: list[int]) -> int:
        count=Counter(nums)
        maxx=-float("inf")
        for ch, num in count.items():
            if ch>maxx and num==1:
                maxx=ch
        return maxx if maxx!=-float("inf") else -1
'''
    create_leetcode_problem_folder(problem_number, problem_title, solution_code)
