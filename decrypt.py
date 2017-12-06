# 345
"""Script to decrypt Caeser cypher encrypted texts."""
from sys import argv

file = argv[1]


def generate_key(shift):
    """Generate Ceasar decyphering key with given shift."""
    lower_case = [chr(l) for l in range(65, 91)]
    upper_case = [chr(l) for l in range(97, 123)]
    a = lower_case + upper_case
    s = lower_case[shift:] + lower_case[:shift] + \
        upper_case[shift:] + upper_case[:shift]
    key = dict(zip(s, a))

    return key


def get_anchors(list_of_words):
    """Small subset of anchor words to test different keys."""
    i = 10
    while True:
        # Filtering for words of length i
        anchors = [x for x in list_of_words if len(x) == i]

        # Ensure a large enough amount of anchors to cross check the key
        if len(anchors) > 2:
            return anchors

        i -= 1


def get_english(anchor):
    """Import only the english words of the same length as anchor."""
    with open("words.txt") as temp:
        all_words = temp.read()

    english_words = [x for x in all_words.split() if len(x) == len(anchor)]

    return english_words


def decrypt(word, key):
    """Decrypt each letter with the key."""
    result = ''
    for character in word:
        if character.isalpha():
            result += key[character]
        else:
            result += character

    return result


def quick_decrypt(anchors, english):
    """Decrypts first anchor, then tries with the others for safety."""
    test = anchors.pop(0)

    for shift in range(1, 27):
        key = generate_key(shift)
        # english words in file are all in lower case
        if decrypt(test.lower(), key) in english:
            # list of bool values
            other_anchors = [decrypt(word.lower(), key)
                             in english for word in anchors]
            if all(other_anchors):
                return key

    else:
        print("Key not found. Unable to decipher message.")


def full_decrypt(encrypted_words, key):
    """Decrypts entire file with the key argument(found with quick_decrypt)."""
    result = [decrypt(word, key) for word in encrypted_words]

    return ' '.join(result)


with open(file, encoding="utf-8") as info:
    text = info.read()

words = text.split()

anchors = get_anchors(words)
english_words = get_english(anchors[0])
key = quick_decrypt(anchors, english_words)
decrypted_text = full_decrypt(words, key)

print(decrypted_text)
