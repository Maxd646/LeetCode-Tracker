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
        f.write("## Description\n\n Time Complexity: O(n)\nSpace Complexity: O(n) \n\n")
        f.write("## Solution\n\nSee [`solution.py`](solution.py)\n")

    print(f"[✅] Created folder and files at: {base_path}")

if __name__ == "__main__":
    problem_number = "pro 3167"
    problem_title = "Better Compression of String"
    solution_code = '''class Solution:
    
"""
from collections import Counter
class Solution:
    def betterCompression(self, compressed: str) -> str:
       
       count= Counter()
       i, n=0, len(compressed)
       while i<n:
           j=i+1
           x=0
           while j<n and  compressed[j].isdigit():
               x=x*10+int(compressed[j])
               j+=1
           count[compressed[i]]+=x
           i=j
       return ''.join(f"{v}{x}" for v, x in count.items())
# or 
class Solution:
    def betterCompression(self, compressed: str) -> str:
        seen={}
        result=""
        i=m=0
        if compressed.isdigit():
            return compressed
        while i<len(compressed)-1:
            if compressed[i].isalpha() and compressed[i]  not in seen :
                m=i
                i+=1
                while i<len(compressed) and compressed[i].isdigit():
                    i+=1
                seen[compressed[m]]=int(compressed[m+1:i])
            elif compressed[i].isalpha() and compressed[i] in seen:
                m=i
                i+=1
                while  i<len(compressed) and compressed[i].isdigit():
                    i+=1
                seen[compressed[m]]+=int(compressed[m+1:i])

        for ch, nun in seen.items():
            result+=(ch+str(nun))
        return result
'''
    create_leetcode_problem_folder(problem_number, problem_title, solution_code)
