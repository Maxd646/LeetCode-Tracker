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
        f.write("## Description\n\n*Time Complexity: O(n))\nSpace Complexity: O(n)*\n\n")
        f.write("## Solution\n\nSee [`solution.py`](solution.py)\n")

    print(f"[✅] Created folder and files at: {base_path}")

if __name__ == "__main__":
    problem_number = "345"
    problem_title = "reverse vowels of a string"
    solution_code = '''
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel= "aeiouAEIOU"
        s=list(s)
        left, right=0, len(s)-1
        while left<right:
            while left<right and s[left] not in vowel:
                left+=1
            while left<right and s[right] not in vowel:
                right-=1
            s[left], s[right] = s[right], s[left]
            right-=1
            left+=1
        return ''.join(s)
            

'''
    create_leetcode_problem_folder(problem_number, problem_title, solution_code)
