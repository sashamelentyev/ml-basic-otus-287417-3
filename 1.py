def to_snake_case(s: str) -> str:
    res = ""

    for i in s:
        if i.isupper():
            res += "_" + i.lower()
        else:
            res += i

    return res.lstrip("_")


def to_camel_case(s: str) -> str:
    return ''.join(word.title() for word in s.split('_'))


text = input('Введите текст: ')

if text.find("_") > -1:
    print(to_camel_case(text))
else:
    print(to_snake_case(text))
