from sys import argv
from termcolor import colored

user = []
words = {}
count = 1
while True:
    try:
        user.append(argv[count])
        count += 1
    except IndexError:
        break

count = 0
found_count = 0
for index, word in enumerate(user):
    words[word] = {}

    for letter in word:
        for check_index, check_word in enumerate(user):
            if index != check_index:
                count += 1
                found = False
                for check_letter in check_word:
                    if letter == check_letter:
                        found = True
                if found and len(user)-1 > count:
                    found_count += 1
                    continue
                elif found:
                    try:
                        if words[word][letter] >= 1:
                            words[word][letter] += 1
                    except KeyError:
                        words[word][letter] = 1
                else:
                    words[word][letter] = 0

for word in user:
    for letter in words[word]:
        if words[word][letter] > 0:
            for i in range(words[word][letter]):
                print(colored(letter, 'green'), end='')
        else:
            print(colored(letter, 'red'), end='')
    print(end=' ')
print()
