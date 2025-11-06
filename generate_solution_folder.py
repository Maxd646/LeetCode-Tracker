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
        f.write("## Description\n\n Time Complexity: O(n*l)\nSpace Complexity: O(1) \n\n")
        f.write("## Solution\n\nSee [`solution.py`](solution.py)\n")

    print(f"[✅] Created folder and files at: {base_path}")

if __name__ == "__main__":
    problem_number = " pro 3696"
    problem_title = "Maxium distance between Unqual Words in Array I1"
    solution_code = '''
class Solution:
    def maxDistance(self, words: List[str]) -> int:
        n = len(words)
        ans = 0
        for i in range(n):
            if words[i] != words[0]:
                ans = max(ans, i + 1)
            if words[i] != words[-1]:
                ans = max(ans, n - i)
        return anss
# or
class Solution:
    def maxDistance(self, words: List[str]) -> int:
        maxx=0
        if words[0]!=word[-1]:
            return len(word)
        i=0
        while i<len(words) and word[i]==words[-1]:
            i+=1
            maxx=max(maxx, len(words)-i)


        j=len(words)-1
        while j>=0 and words[j]==words[0]:
            maxx=max(maxx, j)
            j-=1
        
        return  maxx
# or O(n^2.L)
class Solution:
    def maxDistace(self, word:list[str])->int:
        maxx=0
        for i in range(len(word)):
            for j in range(len(word)):
                if word[i]!=word[j]:
                
                    maxx=max(maxx, abs(j-i)+1)
        return maxx

'''
    create_leetcode_problem_folder(problem_number, problem_title, solution_code)
