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
    problem_number = "pro 3460"
    problem_title = "Longest Common Prefix After at Most One Removal"
    solution_code = '''class Solution:
    class Solution:
    def longestCommonPrefix(self, s: str, t: str) -> int:
        if s ==t:
            return len(s)
        total=n=m=0
        b=0
        while n<len(s) and m<len(t):
            if s[n]==t[m] and b<=1:
                n+=1
                m+=1
                total+=1
            else:
                if n+1<len(s):
                    if s[n+1]==t[m]:
                        n+=1
                        b+=1
                else:
                    break
        return total
'''
    create_leetcode_problem_folder(problem_number, problem_title, solution_code)
