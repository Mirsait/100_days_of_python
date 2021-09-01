
import pandas

alphabet_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
codes = {row.letter: row.code for (_, row) in alphabet_frame.iterrows()}


def to_code(word: str):
    code_list = [codes[letter] for letter in word.upper()]
    return code_list


user_word = input("Enter your word: ")
code_list = to_code(user_word)
print(code_list)
