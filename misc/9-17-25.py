import csv;
import datetime;

def main():
    reader = csv.reader
    for row in reader:
        print(row)


if __name__ == "__main__":
    main()