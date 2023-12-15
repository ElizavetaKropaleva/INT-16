import re


# функция аналогичная title()
def custom_title(input_str):
    def repl(m):
        return m[0].upper()

    result = re.sub(r'\b[a-zа-яё]', repl, input_str)
    return result


if __name__ == '__main__':
    text = input('Enter text: ')
    print('Result: ' + custom_title(text))

