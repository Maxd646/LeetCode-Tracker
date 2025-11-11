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
        f.write("## Description\n\n Time Complexity: O(log n)\nSpace Complexity: O(1) \n\n")
        f.write("## Solution\n\nSee [`solution.py`](solution.py)\n")

    print(f"[✅] Created folder and files at: {base_path}")

if __name__ == "__main__":
    problem_number = "pro 1134 "
    problem_title = "  Armstrong Number"
    solution_code = '''
class Solution:
    def isArmstrong(self, n: int) -> bool:
        m=n
        k=len(str(n))
        summ=0
        while n!=0:
            summ+=(n%10)**k
            n//=10
        return summ==m  
# or
class Solution:
    def isArmstrong(self, n: int) -> bool:
        digits = str(n)
        k = len(digits)
        return sum(int(d)**k for d in digits) == n
'''
    create_leetcode_problem_folder(problem_number, problem_title, solution_code)
