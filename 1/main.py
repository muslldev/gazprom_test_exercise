def format(text:str, max_length:int=70):
    words = text.split()
    lines = []
    current_line = []

    for word in words:
        if current_line:
            if len(" ".join(current_line))+1+len(word) <= max_length:
                current_line.append(word)
            else:
                lines.append(" ".join(current_line))
                current_line = [word]
        else:
            if len(word) <= max_length:
                current_line.append(word)
            else:
                lines.append(word)
                current_line = []

    if current_line:
        lines.append(" ".join(current_line))

    return "\n".join(lines)

text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, 
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in 
voluptate velit esse cillum 
dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

if __name__ == "__main__":
    formatted = format(text)
    print(formatted)