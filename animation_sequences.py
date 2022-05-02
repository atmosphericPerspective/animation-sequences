import re
from pathlib import Path


def find_animation_sequences(path: str):
    p = Path(path)
    if not p.is_dir():
        raise NotADirectoryError(f"Not a directory: '{path}'")

    numbers_by_name = {}
    for filepath in p.iterdir():
        match = re.search(r"(\w+)[.](\d{4})[.]\w+$", str(filepath))
        if match:
            key = match.group(1)
            value = int(match.group(2))
            if numbers_by_name.get(key):
                numbers_by_name[key].append(value)
            else:
                numbers_by_name[key] = [value]

    for name, numbers in numbers_by_name.items():
        ranges = list(_generate_ranges(numbers))  # [1, 4, 2] -> ["1-2", "4"]
        joined_string = ", ".join(ranges)
        print(f"{name}: {joined_string}")


def _generate_ranges(numbers: list[int]):
    numbers.sort()
    first = last = numbers[0]
    for n in numbers[1:]:
        if n - 1 == last:
            last = n
        else:  # Gap detected -> generate range that just ended
            if first == last:
                yield str(first)
            else:
                yield f"{first}-{last}"
            first = last = n
    # Generate last range
    if first == last:
        yield str(first)
    else:
        yield f"{first}-{last}"
