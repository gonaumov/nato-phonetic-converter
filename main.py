from lib.nato_dict import nato_alphabet

def spell_phonetically(text: str) -> str:
    return "\n".join([f'{char} as {nato_alphabet[char.upper()]}' for char in text])

# Interactive loop
print('Type a word or username to spell phonetically. Type "quit" to exit.')
while True:
    user_input = input('Enter text:').strip()
    if user_input.lower() == 'quit':
        print("Exiting. Goodbye!")
        break
    result = spell_phonetically(user_input)
    print(f'Phonetic Spelling: \n{result}')
