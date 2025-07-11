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
        f.write("## Description\n\n*Time Complexity: O(n))\nSpace Complexity: O(1)*\n\n")
        f.write("## Solution\n\nSee [`solution.py`](solution.py)\n")

    print(f"[✅] Created folder and files at: {base_path}")

if __name__ == "__main__":
    problem_number = "151"
    problem_title = "Reverse Words in a String"
    solution_code = '''
class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.strip().split()
        word =reversed(words)
        return " ".join(word)
class Solution:
    def reverseWords(self, s: str) -> str:
        if s==" ":
            return False
        res = []
        i = len(s) - 1

        while i >= 0:
            while i >= 0 and s[i] == ' ':
                i -= 1
            if i < 0:
                break
            j = i
            while i >= 0 and s[i] != ' ':
                i -= 1
            res.append(s[i+1:j+1])
        
        return ' '.join(res)
'''

    create_leetcode_problem_folder(problem_number, problem_title, solution_code)
