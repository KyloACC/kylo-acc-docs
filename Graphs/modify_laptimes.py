import sys

print("lap,driver,laptime")
with open(sys.argv[1], "r") as f:
    for line in f:
        parts = line.strip().split(",")
        parts2 = parts[0].strip().split(" - ")
        print(parts2[0][1:-1] + ",\"" + parts2[1][:-2] +  "\"," + parts[4][1:])