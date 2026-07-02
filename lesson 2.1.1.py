def process_text(text: str) -> list:
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    cleaned_text = text.lower().translate(
        str.maketrans(punctuation, ' ' * len(punctuation))
    )
    return sorted(set(cleaned_text.split()), key=len)


text = input("Enter a text (WITH PROBEL): ")
result = process_text(text)
print(result)