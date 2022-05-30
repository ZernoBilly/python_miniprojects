filename = "letter_counter/data.txt"
invalid_letters = [" ", "'", ".", ",", "'", "-"]


def process_items():
    for row in open("letter_counter/data.txt"):
        row = row.strip()
        letter_freg = {c: row.count(c) for c in set(row)}
        yield letter_freg


letter_freg = {}
for item in process_items():
    for key, value in item.items():
        if key not in invalid_letters:
            letter_freg[key] = letter_freg.get(key, 0) + value

max_value = max(letter_freg, key=letter_freg.get)

print(letter_freg)
