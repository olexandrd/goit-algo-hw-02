from collections import deque


def is_palindrom(text: str) -> bool:
    dq = deque()
    text = text.casefold()
    text = text.replace(" ", "")
    for i in text:
        dq.append(i)
    while len(dq) > 1:
        right = dq.pop()
        left = dq.popleft()
        if right != left:
            return False
    return True


def __main__():
    print("Press Ctrl+C to exit")
    while True:
        try:
            print("Type your string>>>")
            text = input()
            if is_palindrom(text):
                print(f'"{text}" is palindrome')
            else:
                print(f'"{text}" is not palindrome')
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    __main__()
