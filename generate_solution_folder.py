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
    problem_number = " pro 1852"
    problem_title = " Distinct Numbers in Each Subarray"
    solution_code = '''
from collections import Counter
class Solution:
    def distinctNumbers(self, nums: list[int], k: int) -> list[int]:
        freq = Counter(nums[:k])
        res = [len(freq)]
        
        for i in range(k, len(nums)):
            left = nums[i - k]
            freq[left] -= 1
            if freq[left] == 0:
                del freq[left]
            
            freq[nums[i]] += 1
            res.append(len(freq))
        
        return res
# or O(n*k) time
class Solution:
    def distinctNumbers(self, nums: list[int], k: int) -> list[int]:
        total=[]
        for i in range(len(nums)-k+1):
            total.append(len(set(nums[i:i+k])))
        return total
'''
    create_leetcode_problem_folder(problem_number, problem_title, solution_code)
