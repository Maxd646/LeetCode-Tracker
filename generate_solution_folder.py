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
    problem_number = " pro 3687"
    problem_title = "Library Late Fee Calculator "
    solution_code = '''
class Solution:
    def lateFee(self, daysLate: list[int]) -> int:
        summ=0
        for i in range(len(daysLate)):
            if daysLate[i]==1:
                summ+=1
            elif daysLate[i]>1 and daysLate[i]<=5:
                summ+=daysLate[i]*2
            elif daysLate[i]>5:
                summ+=daysLate[i]*3
        return summ
# or
class Solution:
    def lateFee(self, daysLate: list[int]) -> int:
        return sum(1 if d==1 else 2*d if 2=<d<=5 else d*3 for d in dayslate)
'''
    create_leetcode_problem_folder(problem_number, problem_title, solution_code)
