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
    problem_number = "pro 1010"
    problem_title = " Find K-Length Substrings With No Repeated Characters"
    solution_code = '''
class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if len(s)<k or k>26:
            return 0
        if len(s)==k:
            if len(set(len(s)))==len(s):
                return len(s)
            else:
                return 0
        total=0
        for i in range(len(s)-k+1):
            if len(set(s[i:i+k]))==k:
                total+=1
        return total

'''
    create_leetcode_problem_folder(problem_number, problem_title, solution_code)
