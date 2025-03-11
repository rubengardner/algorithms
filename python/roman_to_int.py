class Solution:
    def romanToInt(self, s: str) -> int:
        add_mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sub_mapping = {"I":["V","X"], "X": ["C","L"], "C":["D", "M"]}
        precedent_character="0"
        total_value = 0
        for l in s:
            if l in sub_mapping.get(precedent_character, ""):
                total_value -= add_mapping[precedent_character] * 2
                total_value += add_mapping[l]
            else:
                total_value += add_mapping[l]
            precedent_character = l
        return total_value

roman_3 ="MCMXCIV"
a = Solution().romanToInt(s=roman_3)
print(a)

