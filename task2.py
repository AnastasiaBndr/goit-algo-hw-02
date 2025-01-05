import collections


def check_palindrome(sentense: str):
    parsed_sentence = sentense.strip().replace(' ', '').lower()
    deque = collections.deque(parsed_sentence)

    while len(deque) > 1:
        if deque.popleft() != deque.pop():
            return False
    return True


def main():
    command = input()
    print(check_palindrome(command))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
