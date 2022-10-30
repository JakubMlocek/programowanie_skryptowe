import argparse
import re

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Rename selected functions")
    parser.add_argument("names", help="list of functions names")
    parser.add_argument("file", help="python script name")
    args = parser.parse_args()
    to_replace = re.findall(r"[\w\d_]+:[\w\d_]+", str(args.names))
    file = args.file
    if file:
        with open(file, "r+") as f:
            output = f.read()
            for each in to_replace:
                old_name, new_name = each.split(":")
                output = re.sub(" " + old_name +
                                "(?=\()", repl=" " + new_name, string=output)
            f.seek(0)
            f.write(output)
            f.truncate()

