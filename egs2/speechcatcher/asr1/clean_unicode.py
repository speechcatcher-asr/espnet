import unicodedata

CHAR_REPLACEMENTS = {
    '\u200b': ' ',   # ZERO WIDTH SPACE
    '\u200c': ' ',   # ZERO WIDTH NON-JOINER
    '\u202c': ' ',   # POP DIRECTIONAL FORMATTING
    '\u00ad': '-',   # SOFT HYPHEN
    '\u0007': ' ',   # BELL character
    '\u200e': ' ',   # LEFT-TO-RIGHT MARK
    '\ue000': ' ',   # PRIVATE USE AREA CHAR
    # Add more if needed
}

def clean_line(line):
    cleaned = []
    for c in line:
        if c == '\n':
            cleaned.append(c)  # preserve newline
        elif c in CHAR_REPLACEMENTS:
            cleaned.append(CHAR_REPLACEMENTS[c])
        elif unicodedata.category(c).startswith('C'):
            cleaned.append(' ')
        else:
            cleaned.append(c)
    return ''.join(cleaned)

def clean_file(file_path):
    output_path = file_path + ".cleaned"
    with open(file_path, 'r', encoding='utf-8') as infile, \
         open(output_path, 'w', encoding='utf-8') as outfile:
        for line in infile:
            cleaned_line = clean_line(line)
            outfile.write(cleaned_line)

    print(f"Cleaned file written to: {output_path}")

if __name__ == "__main__":
    clean_file("data/train/text")
