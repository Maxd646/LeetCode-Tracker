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
        f.write("## Description\n\n Time Complexity: O(n+m)\nSpace Complexity: O(n) \n\n")
        f.write("## Solution\n\nSee [`solution.py`](solution.py)\n")

    print(f"[✅] Created folder and files at: {base_path}")

if __name__ == "__main__":
    problem_number = " pro 370"
    problem_title = " Range Addition"
    solution_code = '''
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        re=[0]*length
        for x, y, z in updates:
            re[x]+=z
            if y+1<length:
                re[y+1]-=z
        for i in range(1, length):
            re[i]+=re[i-1]
        return re

# or O(n*m)
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
      re=[0]*length
      for i in range(len(updates)):
         for j in range(updates[i][0], updates[i][1]+1):
            re[j]=re[j]+updates[i][2]
      return re
    
        
'''
    create_leetcode_problem_folder(problem_number, problem_title, solution_code)
