# Leetcode 3136: valid word
# https://leetcode.com/problems/valid-word/

class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        vowels = set("aeiouAEIOU")
        consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")

        has_vowel = has_consonant = False

        for ch in word:
            if not ch.isalnum():
                return False
            if not has_vowel and ch in vowels:
                has_vowel = True
            if not has_consonant and ch in consonants:
                has_consonant = True
            if has_vowel and has_consonant:
                return True  # Early 

        return False
