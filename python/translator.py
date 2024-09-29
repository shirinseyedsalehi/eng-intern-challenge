# Braille Translator - Python Implementation

# Braille alphabet mapping (raised dots as O, empty dots as .)
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......', '.': '..O.OO', ',': '..O...', '?': '..OO.O', '!': '..OOO.', ';': '..O.O.', '-': '..O..O'
}

# Reverse mapping to go from Braille to English
reverse_braille_dict = {v: k for k, v in braille_dict.items()}

def is_braille(input_string):
    """Determine if the input string is Braille based on dot pattern."""
    return all(c in 'O.' for c in input_string)

def translate_to_braille(text):
    """Translate English text to Braille."""
    braille_output = ''
    for char in text.lower():
        if char in braille_dict:
            braille_output += braille_dict[char]
    return braille_output

def translate_to_english(braille_text):
    """Translate Braille to English."""
    english_output = ''
    # Split the input braille into chunks of 6 to represent each Braille character
    for i in range(0, len(braille_text), 6):
        braille_char = braille_text[i:i+6]
        if braille_char in reverse_braille_dict:
            english_output += reverse_braille_dict[braille_char]
    return english_output

def braille_translator(input_string):
    """Main function to translate between Braille and English."""
    if is_braille(input_string):
        return translate_to_english(input_string)
    else:
        return translate_to_braille(input_string)

# Example usage:
print(braille_translator("Hello world"))  # Translates to Braille
print(braille_translator("O.....O.O..."))  # Translates to English



