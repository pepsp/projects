import re
import sys

def main():
    try:
        print(parse(input("HTML: ")))
    except AttributeError as ae:
        print(ae)
        sys.exit(1)



def parse(s):
    try:
        matches = re.search(r"(?:\"|\')?https?://(?:www\.)?youtube\.com/embed/(\w+)(?:\"|\')", s, re.IGNORECASE)
        if matches:
            group = matches.group(1)
            return f"\nhttps://youtu.be/{group}"
    except AttributeError:
        raise AttributeError("None")




if __name__ == "__main__":
    main()
