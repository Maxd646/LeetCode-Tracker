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
    problem_number = "pro 3078"
    problem_title = "Match Alphanumerical Pattern in Matrix I"
    solution_code = '''class Solution:
    
"""
class Solution:
    def findPattern(self, board: List[List[int]], pattern: List[str]) -> List[int]:
        def check(i: int, j: int) -> bool:
            d1 = {}
            d2 = {}
            for a in range(r):
                for b in range(c):
                    x, y = i + a, j + b
                    if pattern[a][b].isdigit():
                        if int(pattern[a][b]) != board[x][y]:
                            return False
                    else:
                        if pattern[a][b] in d1 and d1[pattern[a][b]] != board[x][y]:
                            return False
                        if board[x][y] in d2 and d2[board[x][y]] != pattern[a][b]:
                            return False
                        d1[pattern[a][b]] = board[x][y]
                        d2[board[x][y]] = pattern[a][b]
            return True

        m, n = len(board), len(board[0])
        r, c = len(pattern), len(pattern[0])
        for i in range(m - r + 1):
            for j in range(n - c + 1):
                if check(i, j):
                    return [i, j]
        return [-1, -1]

'''
    create_leetcode_problem_folder(problem_number, problem_title, solution_code)
