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
        f.write("## Description\n\n Time Complexity: O(n))\nSpace Complexity: O(n) \n\n")
        f.write("## Solution\n\nSee [`solution.py`](solution.py)\n")

    print(f"[✅] Created folder and files at: {base_path}")

if __name__ == "__main__":
    problem_number = " pro 293"
    problem_title = " Flip Game"
    solution_code = '''

class Solution:
    def generatePossibleNextMoves(self, currentState: str ) -> list[str]:
        if len(currentState)==1:
            return []
        result=[]
        for i in range(len(currentState)-1):
            if currentState[i:i+2]=="++":
                result.append(currentState[:i]+"--"+currentState[i+2:])
        return result
      # or
      class Solution:
def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        s = list(currentState)
        result = []
        for i, c in enumerate(s[:-1]):
            if c == "+" and s[i + 1] == "+":
                s[i] = s[i + 1] = "-"
                result.append("".join(s))
                s[i] = s[i + 1] = "+"
        return result


'''
    create_leetcode_problem_folder(problem_number, problem_title, solution_code)
