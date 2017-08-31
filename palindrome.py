def inverse(text):
    return text[::-1]


def removecaps(text):
    l = list(text)

    for i in range(len(l)):
        l[i] = l[i].lower()

    return ''.join(l)


def removespaces(text):
    return ''.join(text.split(' '))


def removepunct(text):
    # Tuple of forbidden punctuation
    punct = (',', '.', '!', '?', '...', '-', '\\', '/', '(', ')')
    l = list(text)

    # Replaces with a space because editing a
    # list while iterating it is a pain
    for i in range(len(punct)):  # Goes through the punctuation tuple
        for j in range(len(l)):  # Then goes through each character
            if punct[i] == l[j]:
                l[j] = ' '

    return ''.join(l)


def is_palindrome(text):
    # Simplify the text to just characters without spaces or punct
    simple_text = removecaps(removespaces(removepunct(text)))

    return simple_text == inverse(simple_text)


while True:
    text = input('\n\nEnter word or phrase: ')

    if is_palindrome(text):
        print('\nYes, it is a palindrome.')
    else:
        print('\nNo, it is not a palindrome.')
