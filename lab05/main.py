from tablestats import *


def main():
    path = input().strip()
    with open(path, encoding="utf-8") as table:
        rows = read_rows(table)
    print(rows)

if __name__ == "__main__":
    main()
