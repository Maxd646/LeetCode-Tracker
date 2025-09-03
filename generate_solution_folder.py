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
    problem_number = "163 pro"
    problem_title = "Missing Ranges"
    solution_code = '''
class Soution:
    def findMissingRanges(self, nums:list, lower: int, upper:int)->list[list[int]]:
        if len(nums)==0:
            return [lower, upper]
        num=[]
        if nums[0]>lower:
            num.append([lower+1, nums[0]-1])
        for i in range(1, len(nums)):
            if nums[i]-nums[i-1]>1:
                num.append([nums[i-1]+1, nums[i]-1])   
        if nums[-1]<upper:
            num.append([nums[-1]+1, upper])         
        return num
 
'''
    create_leetcode_problem_folder(problem_number, problem_title, solution_code)
