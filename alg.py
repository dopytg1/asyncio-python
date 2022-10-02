text = 'If I look back I am lost'


def del_letter_from_str(string, letter: str):
    to_change = list(string.lower())
    for i in to_change:
        if i == letter:
            to_change.remove(i)
    return "".join(to_change)


roman_symbols = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


def roman_to_int(to_transfer):
    answer = 0
    for i in to_transfer.upper():
        for key, value in roman_symbols.items():
            if i == key:
                answer += value
    return answer


head = [1, 2, 2, 3]


def is_palindrom(to_check):
    rev = to_check[::-1]
    if rev == head:
        return True
    return False


ransomNote = "a"
magazine = "b"


def can_construct(ransomnote, magazine):
    if ransomnote in magazine:
        return True
    return False


