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
    problem_number = " pro 356"
    problem_title = " Line Refiliction"
    solution_code = '''
class Solution:
    def isReflected(self, nums= list[list[int]])->bool:
        maxx, minx=-float("inf"), float("inf")
        for x, y in nums:
            maxx=max(maxx, x)
            minx=min(minx, x)
        seen=set(tuple(p) for p in nums)
        mid=(maxx+minx)/2
        for x, y in nums:
            row=(2*mid-x, y)
            if row not in seen: 
                return False
        return True
class Solution:
    def isReflected(self, points: list[list[int]]) -> bool:
        maxx, minx=-float("inf"), float("inf")
        seen=set()
        for x, y in points:
            maxx=max(maxx, x)
            minx=min(minx, x)
            seen.add((x, y))
        mid=(maxx+minx)
        return all((mid-x, y) in seen for x, y in points)
    
        
'''
    create_leetcode_problem_folder(problem_number, problem_title, solution_code)
