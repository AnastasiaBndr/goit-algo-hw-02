import re


def check_balanced_brackets(sentence: str):
    stack = []
    parsed_sentence = re.sub(
        '[^/(/)/[/]/{/}]', '', sentence.strip().replace(' ', '').lower())
    opening = "({["
    closing = ")}]"

    for char in parsed_sentence:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack:
                return False
            top = stack.pop()
            if opening.index(top) != closing.index(char):
                return False

    return len(stack) == 0


def main():
    command = "{(5+2)({7*5}([3-4]))}"
    command2 = "{7(1+8)({3-4}([5+7]))*4)}"
    print(check_balanced_brackets(command))
    print(check_balanced_brackets(command2))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
