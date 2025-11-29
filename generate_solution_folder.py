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
    problem_number = "pro 360"
    problem_title = "Sort Transformed Array"
    solution_code = '''class Solution:  
"""
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        num=[]
        for i in range(len(nums)):
            num.append(a*(nums[i]**2) + b*nums[i] + c)
        num.sort()
        return num
"""
'''
    description_text = """ 360.Sort Transformed Array
Description
Given a sorted integer array nums and three integers a, b and c, apply a quadratic function of the form f(x) = ax2 + bx + c to each element nums[i] in the array, and return the array in a sorted order.


Example 1:

Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
Output: [3,9,15,33]
Example 2:

Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
Output: [-23,-5,1,7]


Constraints:

1 <= nums.length <= 200
-100 <= nums[i], a, b, c <= 100
nums is sorted in ascending order."""
    
    create_leetcode_problem_folder(problem_number, problem_title, solution_code, description_text)
