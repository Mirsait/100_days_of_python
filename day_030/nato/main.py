
import pandas

alphabet_frame = pandas.read_csv("alphabet.csv")
codes = {row.letter: row.code for (_, row) in alphabet_frame.iterrows()}


def to_code(word: str):
    code_list = [codes[letter] for letter in word.upper()]
    return code_list

def generate():
    user_word = input("Enter your word: ")
    try:
        code_list = to_code(user_word)
    except KeyError:
        print("Please, enter only letters without numbers.")
        generate()
    else:
        print(code_list)

generate()