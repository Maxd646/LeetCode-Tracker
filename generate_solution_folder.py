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
    problem_number = "pro 1272"
    problem_title = " Remove Interval"
    solution_code = '''
class Solution:
    def removeInterval(self, intervals: list[list[int]], toBeRemoved: list[int])->list[list[int]]:
        re=[]
        for i in range(len(intervals)):
            if intervals[i][1]<toBeRemoved[0] or intervals[i][0]>toBeRemoved[1]:
                re.append(intervals[i])
            else:
                if intervals[i][0]<toBeRemoved[0]:
                    re.append([intervals[i][0], toBeRemoved[0]])
                if intervals[i][1]>toBeRemoved[1]:
                    re.append([toBeRemoved[1], intervals[i][1]])
        return re

'''
    create_leetcode_problem_folder(problem_number, problem_title, solution_code)
