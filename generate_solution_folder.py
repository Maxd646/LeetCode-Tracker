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
    problem_number = "pro 3450"
    problem_title = "Maximum Students on a Single Bench"
    solution_code = '''class Solution:
from collections import Counter
class Solution:
    def maxStudentsOnBench(self, students: list[list[int]]) -> int:
        nums=set(tuple(p) for p in students)
        num=Counter()
        for ch, bnen in nums:
            num[bnen]+=1
        maxx=0
        for _, ch in num.items():
            maxx=max(maxx, ch)
        return maxx
# or
class Solution:
    def maxStudentsOnBench(self, students: List[List[int]]) -> int:
        if not students:
            return 0
        d = defaultdict(set)
        for student_id, bench_id in students:
            d[bench_id].add(student_id)
        return max(map(len, d.values()))
'''
    create_leetcode_problem_folder(problem_number, problem_title, solution_code)
