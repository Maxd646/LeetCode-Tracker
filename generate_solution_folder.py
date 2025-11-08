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
    problem_number = " pro 734"
    problem_title = " Sentence Similarity"
    solution_code = '''
class Solution:  
    def areSentenceSimilar(self, sentence1:str, sentence2:str, simmlilarpar)-> bool:
        if len(sentence1)!=len(sentence2):
            return False
        s={(a, b) for a, b in simmlilarpar}
        m=zip(sentence1, sentence2)
        for a, b in m:
            if (a==b or(a, b) in s or (b, a) in s)  is False:
                return False
        return True
    # or 
class Solution:  
    def areSentenceSimilar(self, sentence1:str, sentence2:str, simmlilarpar)-> bool:
        if len(sentence1)!=len(sentence2):
            return False
        if len(sentence1)!=len(sentence2):
            return False
        s={(a, b) for a, b in simmlilarpar}
        return all(a==b or (a, b) in s or (b, a) in s for a, b in zip(sentence1, sentence2))
'''
    create_leetcode_problem_folder(problem_number, problem_title, solution_code)
