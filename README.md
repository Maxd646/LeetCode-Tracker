# LeetCode Tracker 🧠📘

This repository contains my personal solutions to [LeetCode](https://leetcode.com/) problems, organized by problem number and title.

Each problem includes:

+ ✅ A clean, efficient **Python solution**
+ 📄 A `README.md` with **problem description**, examples, and explanations
+ 📁 A folder under `leetcode-solutions/` named using the problem number and title

---

## 🚀 Purpose

This repository helps me:

+ Practice daily coding and problem-solving
+ Track my learning progress over time
+ Prepare for technical interviews
+ Build a clear and organized portfolio of LeetCode solutions

---

## 📁 Folder Structure

```
LeetCode-Tracker/
├── generate_solution_folder.py       # Script to auto-create solution folders
├── README.md                         # ← This file
└── leetcode-solutions/
    ├── 2129-capitalize-the-title/
    │   ├── solution.py
    │   └── README.md
    ├── 217-contains-duplicate/
    │   ├── solution.py
    │   └── README.md
    └── ...more problems
```

---

## ⚙️ How I Add New Problems

To keep things clean and automatic, I use a Python script:

### Steps:

1. Open `generate_solution_folder.py`
2. Edit these:
   - `problem_number`
   - `problem_title`
   - `solution_code`
   - `problem_description`
3. Run:

```bash
python generate_solution_folder.py
```

4. Then push to GitHub:

```bash
git add leetcode-solutions/<problem-folder>/
git commit -m "Add Leetcode <number>: <title> solution"
git push
```

---

## ✅ Example Problem

### [Leetcode 2129 – Capitalize the Title](https://leetcode.com/problems/capitalize-the-title/)

Capitalize each word in the title such that:

- Words with 1–2 letters → lowercase
- Words with 3+ letters → Capitalized (first letter uppercase, rest lowercase)

```python
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return " ".join(
            word.lower() if len(word) <= 2 else word.capitalize()
            for word in title.split()
        )
```

---

## 📫 Contact

- **GitHub**: [Maxd646](https://github.com/Maxd646)
- **Email**: ethiomiracle2017@gmail.com

---

## 📝 License

This project is licensed under the **MIT License**.  
You’re welcome to use, copy, or contribute freely.
