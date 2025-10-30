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
        f.write("## Description\n\n Time Complexity: O(n))\nSpace Complexity: O(1) \n\n")
        f.write("## Solution\n\nSee [`solution.py`](solution.py)\n")

    print(f"[✅] Created folder and files at: {base_path}")

if __name__ == "__main__":
    problem_number = " pro 25"
    problem_title = " Shortest Word Distance III "
    solution_code = '''

class Solution:
    def shortestWordDistance(self, wordsDic: list[str], word1: str, word2: str) -> int:
        index1, index2=-1, -1
        same =(word1==word2)
        minno=float("inf")
        for i, words in enumerate(wordsDic):
            if words==word1:
                if same and index1!=-1:
                    minno=min(minno, i-index1)
                index1=i
            elif words==word2:
                index2=i
            if not same and index1!=-1 and  index2!=-1:
                minno=min(minno, abs(index1-index2))
        return minno
                  

'''
    create_leetcode_problem_folder(problem_number, problem_title, solution_code)
