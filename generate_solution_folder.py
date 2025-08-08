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
    problem_number = "434"
    problem_title = "Count Segments in a String"
    solution_code = '''

class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        InSegment = False
        
        for char in s:
            if char != ' ':
                if not InSegment:
                    count += 1
                    InSegment = True
            else:
                InSegment = False
        
        return count

# or
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split()) if s else 0   
        
'''
    create_leetcode_problem_folder(problem_number, problem_title, solution_code)
