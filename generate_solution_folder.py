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
        f.write("## Description\n\n Time Complexity: O(n)\nSpace Complexity: O(1) \n\n")
        f.write("## Solution\n\nSee [`solution.py`](solution.py)\n")

    print(f"[✅] Created folder and files at: {base_path}")

if __name__ == "__main__":
    problem_number = " 209"
    problem_title = " Minimum Size Subarray Sum"
    solution_code = '''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        summ, x=0, 0
        minn=float("inf")
        for i in range(len(nums)):
            summ+=nums[i]
            while summ>=target:
                minn=min(minn, i-x+1)
                summ-=nums[x]
                x+=1
        return minn if minn!=float("inf") else 0
# or
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        summ, x=0, 0
        minn=float("inf")
        for i in range(len(nums)):
            summ+=nums[i]
            while summ>target:
                summ-=nums[x]
                x+=1
            if minn==target:
                minn=min(minn, i-x+1)
        return minn if minn!=float("inf") else 0
'''
    create_leetcode_problem_folder(problem_number, problem_title, solution_code)
