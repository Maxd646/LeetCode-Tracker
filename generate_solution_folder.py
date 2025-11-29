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
    problem_number = "pro 2229"
    problem_title = " Check if an Array Is Consecutive"
    solution_code = '''class Solution:  
"""
class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        mi, mx = min(nums), max(nums)
        n = len(nums)
        return len(set(nums)) == n and mx == mi + n - 1
#or 
class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        x=len(nums)
        n=min(nums)
        for i in range(n, n + x):
            if i not in set(nums):
                return False
        return True
"""
'''
    description_text = """ You are given a string array features where features[i] is a single word that represents the name of a feature of the latest product you are working on. You have made a survey where users have reported which features they like. You are given a string array responses, where each responses[i] is a string containing space-separated words.

The popularity of a feature is the number of responses[i] that contain the feature. You want to sort the features in non-increasing order by their popularity. If two features have the same popularity, order them by their original index in features. Notice that one response could contain the same feature multiple times; this feature is only counted once in its popularity.

Return the features in sorted order.

 

Example 1:

Input: features = ["cooler","lock","touch"], responses = ["i like cooler cooler","lock touch cool","locker like touch"]
Output: ["touch","cooler","lock"]
Explanation: appearances("cooler") = 1, appearances("lock") = 1, appearances("touch") = 2. Since "cooler" and "lock" both had 1 appearance, "cooler" comes first because "cooler" came first in the features array.

Example 2:

Input: features = ["a","aa","b","c"], responses = ["a","a aa","a a a a a","b a"]
Output: ["a","aa","b","c"]
 

Constraints:

1 <= features.length <= 104
1 <= features[i].length <= 10
features contains no duplicates.
features[i] consists of lowercase letters.
1 <= responses.length <= 102
1 <= responses[i].length <= 103
responses[i] consists of lowercase letters and spaces.
responses[i] contains no two consecutive spaces.
responses[i] has no leading or trailing spaces.
"""
    
    create_leetcode_problem_folder(problem_number, problem_title, solution_code, description_text)
