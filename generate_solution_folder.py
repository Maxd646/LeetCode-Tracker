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
        f.write("## Description\n\n Time Complexity: O(n^2)\nSpace Complexity: O(1) \n\n")
        f.write("## Solution\n\nSee [`solution.py`](solution.py)\n")

    print(f"[✅] Created folder and files at: {base_path}")

if __name__ == "__main__":
    problem_number = "pro 3400"
    problem_title = "Maximum Number of Matching Indices After Right Shifts"
    solution_code = '''class Solution:
class Solution:
    def maximumMatchingIndices(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        ans = 0
        for k in range(n):
            t = sum(nums1[(i + k) % n] == x for i, x in enumerate(nums2))
            ans = max(ans, t)
        return ans
# or 
class Solution:
    def maximumMatchingIndices(self, nums1: list[int], nums2: list[int]) -> int:
        left, right=0, len(nums1)-1
        maxx=i=no=0
        while i<len(nums1):
            nums1=nums1[i:]+nums1[:i]
            no=0
            left, right=0, len(nums1)-1
            while left<right:
                if nums1[left]==nums2[left]:
                    no+=1
                    left+=1
                if nums1[right]==nums2[right]:
                    no+=1
                    right-=1
                else:
                    left+=1
                    right-=1
                maxx=max(no, maxx)
            i+=1
        return maxx
'''
    create_leetcode_problem_folder(problem_number, problem_title, solution_code)
