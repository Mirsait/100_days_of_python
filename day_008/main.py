from arts import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

# for terminal clearing
print('\033c')

print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(text, shift, direction):
    result_text = ""
    if direction == "decode":
        shift *= -1
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        if new_position >= len(alphabet):
            new_position -= len(alphabet)
        elif new_position < 0:
            new_position += len(alphabet)
        result_text += alphabet[new_position]
    print(f"{direction}d text: {result_text}")


caesar(text, shift, direction)
