# from collections import Counter
#
# def symbol_probabilities(text: str) -> dict[str, float]:
#     total = len(text)
#     counts = Counter(text)
#     return {s: c / total for s, c in counts.items()}
#
#
# def format_table(probs: dict[str, float]) -> str:
#     lines = ["| символ | частота |", "|--------|----------|"]
#     for s, p in probs.items():
#         lines.append(f"| {s} | {p:.3f} |")
#     return "\n".join(lines)
#
#
# text = input()
# probs = symbol_probabilities(text)
# print(format_table(probs))

text_input = input("Введіть рядок для аналізу: ")


def symbol_probabilities(text: str) -> dict[str, float]:
    chars = len(text)
    set_text = set(text)
    probabilities = {}

    # Потрібно лише порахувати і повернути, без друку
    for item in set_text:
        count = text.count(item)
        frequency = count / chars
        probabilities[item] = frequency

    return probabilities


def format_table(probs: dict[str, float]) -> None:
    print("Результат аналізу:")
    print("| символ | частота |")
    print("|--------|---------|")

    # Виведення результату тут
    for item, frequency in probs.items():
        print(f"|   {item}    | {frequency:.3f}   |")

    print("|--------|---------|")


# Спочатку обчислюємо частоти
probabilities = symbol_probabilities(text_input)

# Потім виводимо таблицю
format_table(probabilities)


