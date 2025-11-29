import os

def slugify(title):
    return title.strip().lower().replace(" ", "-")

def create_leetcode_problem_folder(problem_number, title, solution_code, description=""):
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
        f.write("## Description\n\n")
        if description:
            f.write(description + "\n\n")
        else:
            f.write("No description provided.\n\n")
        f.write("## Complexity Analysis\n\n")
        f.write("Time Complexity: O(n log n)\n")
        f.write("Space Complexity: O(n)\n\n")
        f.write("## Solution\n\nSee [`solution.py`](solution.py)\n")

    print(f"[✅] Created folder and files at: {base_path}")

if __name__ == "__main__":
    problem_number = "pro 3078"
    problem_title = "Match Alphanumerical Pattern in Matrix I"
    solution_code = '''class Solution:  
"""
Your solution code here
"""
'''
    description_text = """Given a matrix of alphanumerical characters, 
find if the matrix matches a given alphanumerical pattern. 
Return True if the pattern exists, otherwise False."""
    
    create_leetcode_problem_folder(problem_number, problem_title, solution_code, description_text)
