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
        f.write("## Description\n\n Time Complexity: O(n*k)\nSpace Complexity: O(k) \n\n")
        f.write("## Solution\n\nSee [`solution.py`](solution.py)\n")

    print(f"[✅] Created folder and files at: {base_path}")

if __name__ == "__main__":
    problem_number = " pro 3672"
    problem_title = "Sum of Weighted Modes in Subarrays  "
    solution_code = '''
from collections import Counter
class Solution:
    def modeWeight(self, num1: list[int], k: int) -> int:
        summ=0
        for i in range(len(num1)-k+1):
            count=Counter(num1[i:i+k])
            maxx=0
            num=0
            for j, fr in count.items():
                if fr>maxx:
                    maxx=fr
                    num=j
                elif fr==maxx:
                    num=min(num, j)
            summ+=num*maxx
        return summ
'''
    create_leetcode_problem_folder(problem_number, problem_title, solution_code)
