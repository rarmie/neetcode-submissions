class Solution:
    def isPalindrome(self, s: str) -> bool:
        reversed_list = []
        original_str_list = []

        for letter in s:
            if letter.isalnum():
                reversed_list.insert(0, letter.lower())
                original_str_list.append(letter.lower())

        return reversed_list == original_str_list

