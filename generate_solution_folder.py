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
        f.write("## Description\n\n*Time Complexity: O(n))\nSpace Complexity: O(n)*\n\n")
        f.write("## Solution\n\nSee [`solution.py`](solution.py)\n")

    print(f"[✅] Created folder and files at: {base_path}")

if __name__ == "__main__":
    problem_number = 88
    problem_title = "Merge Sorted Array"
    solution_code = '''
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = []
        i = len(num) - 1

        while i >= 0 or k > 0:
            if i >= 0:
                k += num[i]
            res.append(k % 10)
            k //= 10
            i -= 1

        return res[::-1]  
# or     
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        m= int(''.join(str(digit) for digit in num))
        total = k+m
        return [int(d) for d in str(total)]
'''

    create_leetcode_problem_folder(problem_number, problem_title, solution_code)
