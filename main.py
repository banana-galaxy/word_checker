import sys

if len(sys.argv) < 3:
    print("Please enter two words to check against each other")
    quit()

first = list(sys.argv[1])
second = list(sys.argv[2])

i = 0
count = 0
nope = ""
for letter in first:
    for letter2 in second:
        if letter2 == letter:
            i += 1
    if i > 0:
        count += 1
    else:
        nope += f"{letter} "

if count == len(first) and count == len(second):
    print("All good")
else:
    print(f"Nope, these don't match: {nope}")