def spell_phonetically(text: str) -> str:
    return f'Hi, {text}'

# Interactive loop
print('Type a word or username to spell phonetically. Type "quit" to exit.')
while True:
    user_input = input('Enter text:').strip()
    if user_input.lower() == 'quit':
        print("Exiting. Goodbye!")
        break
    result = spell_phonetically(user_input)
    print('Phonetic Spelling:', result)
