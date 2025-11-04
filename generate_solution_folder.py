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
    problem_number = " pro 408"
    problem_title = "Valid Word Abbreviation"
    solution_code = '''
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i=j=0
        m, n=len(word), len(abbr)
        while i<m and j<n:
            if abbr[j].isalpha():
                if word[i]!=abbr[j]:
                    return False
                j+=1
                i+=1
            else:
                if abbr[j]=="0" or int(abbr[j])==0:
                    return False
                num=0
                while j<n and abbr[j].isdigit():
                    num=num*10+int(abbr[j])
                    j+=1
                i+=num
        return j==len(abbr) and i==len(word)
'''
    create_leetcode_problem_folder(problem_number, problem_title, solution_code)
