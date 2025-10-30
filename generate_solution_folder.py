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
        f.write("## Description\n\n Time Complexity: O(n))\nSpace Complexity: O(1) \n\n")
        f.write("## Solution\n\nSee [`solution.py`](solution.py)\n")

    print(f"[✅] Created folder and files at: {base_path}")

if __name__ == "__main__":
    problem_number = " pro 186"
    problem_title = " Reverse Words in a String II"
    solution_code = '''

class Solution:
    class Solution:
    def reverseWords(self, s: list[str]) -> None:
        left, right=0, len(s)-1
        while left<right:
            s[left], s[right]=s[right], s[left]
            left+=1
            right-=1
        j=0
        for i in range(len(s)+1):
            if i==len(s) or s[i]==' ':
                start, end=j, i-1
                while start<end:
                    s[start], s[end]=s[end], s[start]
                    start+=1
                    end-=1
                j=i+1

'''
    create_leetcode_problem_folder(problem_number, problem_title, solution_code)
