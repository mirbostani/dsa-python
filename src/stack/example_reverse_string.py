def reverse_word(word: str) -> str:
    stack = []

    # Push chars onto the stack
    for char in word:
        stack.append(char)

    # Pop chars from the stack and concatenate them
    word_reversed = ""
    while stack:
        word_reversed += stack.pop()

    return word_reversed

if __name__ == "__main__":
    word = "abc"
    rword = reverse_word(word)
    print(rword) # "cba"