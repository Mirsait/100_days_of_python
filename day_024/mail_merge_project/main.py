
def read_names():
    with open(file="Input/Names/invited_names.txt", mode='r') as file:
        names = [name.strip('\n') for name in file.readlines()]
        return names

def get_letter_template():
    with open(file="Input/Letters/starting_letter.txt", mode='r' ) as file:
        letter = file.read()
        return letter

def save_letter(name, text):
    with open(file=f"Output/ReadyToSend/{name}.txt", mode='w') as file:
        file.write(text)


names = read_names()
template = get_letter_template()
PLACEHOLDER = "[name]"

for name in names:
    new_letter = template.replace(PLACEHOLDER, name)
    save_letter(name, new_letter)