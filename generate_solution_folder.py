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
        f.write("## Description\n\n Time Complexity: O(m*n)\nSpace Complexity: O(n) \n\n")
        f.write("## Solution\n\nSee [`solution.py`](solution.py)\n")

    print(f"[✅] Created folder and files at: {base_path}")

if __name__ == "__main__":
    problem_number = "pro 1198"
    problem_title = "Find Smallest Common Element in All Rows"
    solution_code = '''

class Solution:
    def smallestCommonElement(self, mat: list[list[int]]) -> int:
        re=set(mat[0]).intersection(set(mat[1]))
        for i in range(2, len(mat)):
            re=re.intersection(set(mat[i]))
        if not re:
            return -1
        return min(re)
## or
from collections import Counter
class Solution:
    def smallestCommonElement(self, mat: list[list[int]]) -> int:
        cc=Counter()
        for x in mat:
            for m in x:
                cc[m]+=1
                if cc[m]==len(mat):
                    return m
        return -1
'''
    create_leetcode_problem_folder(problem_number, problem_title, solution_code)
