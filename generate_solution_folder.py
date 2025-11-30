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
        f.write("Time Complexity: O(n)\n")
        f.write("Space Complexity: O(1)\n\n")
        f.write("## Solution\n\nSee [`solution.py`](solution.py)\n")

    print(f"[✅] Created folder and files at: {base_path}")

if __name__ == "__main__":
    problem_number = "pro 3631"
    problem_title = " Sort Threats by Severity and Exploitability"
    solution_code = '''class Solution:  
"""
class Solution:
    def sortThreats(self, threats: List[List[int]]) -> List[List[int]]:
        return sorted(threats,key=lambda x:(-(2 * x[1] + x[2]), x[0]))
# or 
class Solution:
    def sortThreats(self, threats: List[List[int]]) -> List[List[int]]:
        score=[0]*len(threats)
        for i in range(len(threats)):
            score[i] = 2 * threats[i][1] + threats[i][2]
            for j in range(i+1, len(threats)):
                score[j] = 2 * threats[j][1] + threats[j][2]
                if score[i]<score[j]:
                    threats[i], threats[j]=threats[j], threats[i]
                elif score[i]==score[j] and threats[i][0]>threats[j][0]:
                    threats[i], threats[j]=threats[j], threats[i] 
        return threats
            
# or
class Solution:
    def sortThreats(self, threats: List[List[int]]) -> List[List[int]]:
        threats.sort(key=lambda x:(-(2 * x[1] + x[2]), x[0]))
        return threats
"""
'''
    description_text = """ 
You are given a 2D integer array threats, where each threats[i] = [IDi, sevi​, expi]

IDi: Unique identifier of the threat.
sevi: Indicates the severity of the threat.
expi: Indicates the exploitability of the threat.
The score of a threat i is defined as: score = 2 × sevi + expi

Your task is to return threats sorted in descending order of score.


If multiple threats have the same score, sort them by ascending ID​​​​​​​.

 

Example 1:

Input: threats = [[101,2,3],[102,3,2],[103,3,3]]

Output: [[103,3,3],[102,3,2],[101,2,3]]

Explanation:

Threat	ID	sev	exp	Score = 2 × sev + exp
threats[0]	101	2	3	2 × 2 + 3 = 7
threats[1]	102	3	2	2 × 3 + 2 = 8
threats[2]	103	3	3	2 × 3 + 3 = 9
Sorted Order: [[103, 3, 3], [102, 3, 2], [101, 2, 3]]

Example 2:

Input: threats = [[101,4,1],[103,1,5],[102,1,5]]

Output: [[101,4,1],[102,1,5],[103,1,5]]

Explanation:​​​​​​​

Threat	ID	sev	exp	Score = 2 × sev + exp
threats[0]	101	4	1	2 × 4 + 1 = 9
threats[1]	103	1	5	2 × 1 + 5 = 7
threats[2]	102	1	5	2 × 1 + 5 = 7
threats[1] and threats[2] have same score, thus sort them by ascending ID.

Sorted Order: [[101, 4, 1], [102, 1, 5], [103, 1, 5]]

 


Constraints:

1 <= threats.length <= 105
threats[i] == [IDi, sevi, expi]
1 <= IDi <= 106
1 <= sevi <= 109
1 <= expi <= 109
All IDi are unique
"""
    
    create_leetcode_problem_folder(problem_number, problem_title, solution_code, description_text)
