import unicodedata

def is_printable_unicode(char):
    category = unicodedata.category(char)
    # Categories starting with 'C' are control chars, format chars, etc.
    return not category.startswith('C')

def find_non_printable_unicode_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, start=1):
            if line[-1] == '\n':
                line = line[:-1]
            non_printables = [(i, c, unicodedata.name(c, "UNKNOWN"), f"U+{ord(c):04X}")
                              for i, c in enumerate(line)
                              if not is_printable_unicode(c)]
            if non_printables:
                print(f"Line {line_num} has non-printable Unicode characters:")
                print(f"  Text: {line.strip()}")
                for idx, char, name, code in non_printables:
                    print(f"    - Pos {idx}: '{char}' ({name}, {code})")

if __name__ == "__main__":
    find_non_printable_unicode_lines("data/train/text")
