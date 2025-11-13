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
        f.write("## Description\n\n Time Complexity: O(log n)\nSpace Complexity: O(1) \n\n")
        f.write("## Solution\n\nSee [`solution.py`](solution.py)\n")

    print(f"[✅] Created folder and files at: {base_path}")

if __name__ == "__main__":
    problem_number = "pro 1150 "
    problem_title = " Check If a Number Is Majority Element in a Sorted Array"
    solution_code = '''
class Solution:
    def isMajorityElement(self, nums: list[int], target: int) -> bool:
        left, right=0, len(nums)-1
        stat=-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                stat=mid
                right=mid-1
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        if stat==-1:
            return False
        if stat+len(nums)//2<len(nums) and nums[stat+len(nums)//2]==target:
            return True
        return False
# or
class Solution:
    def isMajorityElement(self, nums: list[int], target: int) -> bool:
    return nums.count(target)>len(nums)//2
'''
    create_leetcode_problem_folder(problem_number, problem_title, solution_code)
