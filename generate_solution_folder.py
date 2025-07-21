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
        f.write("## Description\n\n*Time Complexity: O(n))\nSpace Complexity: O(1)*\n\n")
        f.write("## Solution\n\nSee [`solution.py`](solution.py)\n")

    print(f"[✅] Created folder and files at: {base_path}")

if __name__ == "__main__":
    problem_number = "190"
    problem_title = "Reverse Bits"
    solution_code = '''

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):       
            result <<= 1          
            result |= n & 1     
            n >>= 1               
        return result
# or
class Solution:
    def reverseBits(self, n: int) -> int:
        rem= 0
        re=''
        while n>0:
            reme=n%2
            re=str(reme)+re
            n//=2
        re = re.zfill(32)
        reverse = re[::-1]
        return int(reverse, 2)

'''

    create_leetcode_problem_folder(problem_number, problem_title, solution_code)
