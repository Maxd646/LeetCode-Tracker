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
    problem_number = " pro 3682"
    problem_title = " Minimum Index Sum of Common Elements "
    solution_code = '''
class Solution:
    def lateFee(self, num1: list[int], num2: list[int]) -> int:
        minn=float("inf")
        seen={num1[i]:i for i in range(len(num1))}
        for i in range(len(num2)):
            if num2[i] in seen:
                minn=min(minn, i+ seen[num2[i]])
        return minn if minn!=float("inf") else -1

 # or for O(n*L)
class Solution:
    def lateFee(self, num1: list[int], num2: list[int]) -> int:
        minn=float("inf")
        seen=set(num1)
        for i in range(len(num2)):
            if num2[i] in seen:
                j=num1.index(num2[i])
                minn=min(minn, i+ j)
        return minn if minn!=float("inf") else -1

'''
    create_leetcode_problem_folder(problem_number, problem_title, solution_code)
