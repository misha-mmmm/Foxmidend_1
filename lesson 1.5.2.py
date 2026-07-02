line_length = 80
line_symbol = "-"

def print(*args, **kwargs):
    __builtins__.print(line_symbol * line_length)
    __builtins__.print()
    __builtins__.print(*args, **kwargs)
    __builtins__.print()
    __builtins__.print(line_symbol * line_length)

print("Hello, world!")
print("Second call to print()")