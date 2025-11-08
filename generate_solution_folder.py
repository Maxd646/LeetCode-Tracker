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
    problem_number = " pro 760"
    problem_title = " Find Anagram Mappings"
    solution_code = '''
# last occurance
class Solution:  
    def anagramMapper(self, num1:list[int], num2:list[int])-> list[int]:
        seen={num:i for i, num in enumerate(num2)}
        return [seen[num] for num in num1]
# or
class Solution:  
    def anagramMapper(self, num1:list[int], num2:list[int])-> list[int]:
        seen={num:i for i, num in enumerate(num2)}
        for num in num1:
            re.append(seen[num])

# for the first occurance
class Solution:  
    def anagramMapper(self, num1:list[int], num2:list[int])-> list[int]:
        seen={}
        for i, num in enumerate(num2):
            if num not in seen:
                seen[num]=i
        re=[]
        for nu in num1:
            re.append(seen[nu])
        return re

    
'''
    create_leetcode_problem_folder(problem_number, problem_title, solution_code)
