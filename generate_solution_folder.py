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
        f.write("## Description\n\n Time Complexity: O(logn)\nSpace Complexity: O(1) \n\n")
        f.write("## Solution\n\nSee [`solution.py`](solution.py)\n")

    print(f"[✅] Created folder and files at: {base_path}")

if __name__ == "__main__":
    problem_number = " pro 3581"
    problem_title = "Count Odd Letters from Number"
    solution_code = '''
class Solution:
    def search(self, reader, target):
        left, right=0, 10000
        while left<right:
            mid=(left+right)//2
            if reader.get(mid)==target:
                return mid
            elif reader.get(mid)>target:
                right=mid+1
            else:
                left+=1
        retur -1
# or
class Solution:
    def search(self, reader, target):
        left, right=0, 10001
        while left<right:
            mid=(left+right)//2
            if reader.get(mid)>=target:
                right=mid
            else:
                left=mid+1
        return left if reader.get(left) ==target else -1  
'''
    create_leetcode_problem_folder(problem_number, problem_title, solution_code)
