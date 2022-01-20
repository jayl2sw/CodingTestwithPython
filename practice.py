def get_secret_number(string):
    total = 0
    for char in string:
        total += ord(char)
    return total

def get_strong_word(str1, str2):
    a1 = get_secret_number(str1)
    a2 = get_secret_number(str2)
    if a1 > a2:
        return str1
    else:
        return str2






print(get_strong_word('z', 'a'),
get_strong_word('tom', 'john') )