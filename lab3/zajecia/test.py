import argparse
import re

def abc(filePath, text, subs, flags=0):
    with open(file_path, "r+") as file:
        file_contents = file.read()
        text_pattern = re.compile(text, flags)
        file_contents = text_pattern.sub(subs, file_contents)
        file.seek(0)
        file.truncate()
        file.write(file_contents)
        zmienna = "changer()"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Renames selected functions')
    parser.add_argument('names', metavar='names', type=str, nargs='+',
                        help='List of function names')

    parser.add_argument('file', metavar='file', type=str, nargs='?',
                        help='Python script name ')

    file_path="review.txt"
    text="boundation"
    subs="foundation"
    abc(file_path, text, subs)

    args = parser.parse_args()
    see(args)