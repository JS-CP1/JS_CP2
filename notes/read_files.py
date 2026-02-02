# JS, 1st, Reading Files Notes

import csv

while True:
    try:
        with open("notes/reading.txt", "r") as file:
            for line in file:
                print(f"Hello, {line.strip()}")
    except:
        print("That file was not found.")
    else:
        print("code ends")
        break

try:
    with open("notes/testing_sheet.csv", mode = "r") as csv_file:
        content = csv.reader(csv_file)
        headers = next(content)
        rows = []
        for line in content:
            rows.append({headers[0]: line[0], headers[1]: line[1]})
except:
    print("That file was not found.")
else:
    for line in rows:
        print(line)