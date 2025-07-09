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
        f.write("## Description\n\n*Time Complexity: O(log n))\nSpace Complexity: O(n)*\n\n")
        f.write("## Solution\n\nSee [`solution.py`](solution.py)\n")

    print(f"[✅] Created folder and files at: {base_path}")

if __name__ == "__main__":
    problem_number = "504"
    problem_title = "Base 7"
    solution_code = '''
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        sign = '-' if num < 0 else ''
        num = abs(num)
        digits = []
        while num:
            digits.append(str(num % 7))
            num //= 7
        return sign + ''.join(reversed(digits))
# or 
def convertToBase7(self, num: int) -> str:
        if num==0:
            return '0'
        re = ""
        negative= num<0
        if num<0:
            num=abs(num)
        while num>0:
            re= str(num%7)+re
            num//=7
        if negative:
            re='-'+re
        return re
'''

    create_leetcode_problem_folder(problem_number, problem_title, solution_code)
