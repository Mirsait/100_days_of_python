import os

file_name = "data.txt"

def create_file():
    if not os.path.isfile(file_name):
        save_score(0)

def save_score(score):
    with open(file=file_name, mode="w") as file:
        file.write(f"highscore:{score}")


def get_high_score():
    with open(file=file_name, mode="r") as file:
        score = file.readline().split(':')[1]
        return int(score)