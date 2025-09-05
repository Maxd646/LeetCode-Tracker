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
    problem_number = "pro 243"
    problem_title = "Shortest Distance"
    solution_code = '''

class Soution:
    def shortestDistance(self, wordsDict:list[str], word1: str, word2:str)->int:
        d= float("inf")
        j, k=-1, -1
        for i in range(len(nums)):
            if lower==nums[i]:
                k=i
            elif upper==nums[i]:
                j=i
            if k!=-1 and j!=-1:
                d=min(d, abs(j-k))
        return d
    # or 
        for i, ch in enumerate(nums):
            if ch==lower:
                k=i
            elif ch==upper:
                j=i
            if k!=-1 and j!=-1:
                d=min(d, abs(k-j))
        return d
 
'''
    create_leetcode_problem_folder(problem_number, problem_title, solution_code)
