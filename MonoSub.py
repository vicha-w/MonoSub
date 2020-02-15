import os
import argparse
import pickle

atoz = "abcdefghijklmnopqrstuvwxyz".upper()
dictionary = {}
for char in atoz: dictionary[char] = '.'

parser = argparse.ArgumentParser()
parser.add_argument("inputfile")
args = parser.parse_args()

codefile = open(args.inputfile, "r")
codelines = [line.strip().upper() for line in codefile.readlines()]

def substitute(text):
    res = ""
    for char in text:
        if char in dictionary.keys(): res += dictionary[char]
        else: res += char
    return res

def print_message():
    os.system("clear")
    for line in codelines:
        print()
        print("   " + line)
        print("   " + substitute(line))
    print()

autofreq = True
commandlist = "add remove clear reset frequency autofreq summary save load quit exit"

while True:
    print_message()
    if autofreq:
        letter_count = {}
        for key in dictionary.keys(): letter_count[key] = 0
        for line in codelines:
            for char in line: 
                if char in letter_count.keys(): letter_count[char] += 1
        letter_count_tuple = [(k, v) for k, v in letter_count.items()]
        letter_count_tuple.sort(key = lambda x: -x[1])

        count = 0
        for k, v in letter_count_tuple:
            print("{}: {}".format(k, v), end = '\t')
            count += 1
            if count == 6: 
                print()
                count = 0
        print("\n")
    print("Commands: " + commandlist + '\n')
    command = ""
    while command == "":
        try:
            command = input("> ")
            if command in ["quit", "exit"]:
                os.system("clear")
                exit()
            elif command == "":
                continue
            elif command.split(' ')[0] == "add":
                if len(command.split(' ')) != 3:
                    print("Usage: add <source-word> <dest-word>")
                    command = ""
                    continue
                source_word = command.split(' ')[1]
                dest_word   = command.split(' ')[2]
                if len(source_word) != len(dest_word):
                    print("add: Length mismatch.")
                    command = ""
                    continue
                for s, d in zip(source_word.upper(), dest_word.upper()):
                    if s in dictionary.keys(): dictionary[s] = d
            elif command.split(' ')[0] == "remove":
                if len(command.split(' ')) != 2:
                    print("Usage: remove <char>")
                    command = ""
                    continue
                elif len(command.split(' ')[1]) != 1:
                    print("remove: Remove one character at a time!")
                    command = ""
                    continue
                dictionary[command.split(' ')[1].upper()] = '.'
            elif command == "clear":
                continue
            elif command == "reset":
                for key in dictionary.keys():
                    dictionary[key] = '.'
            elif command.split(' ')[0] == "autofreq":
                if len(command.split(' ')) != 2:
                    print("Usage: autofreq (on/off)")
                    command = ""
                    continue
                if command.split(' ')[1] == "on":
                    print("Auto frequency printing is ON.")
                    autofreq = True
                    command = ""
                    continue
                elif command.split(' ')[1] == "off":
                    print("Auto frequency printing is OFF.")
                    autofreq = False
                    command = ""
                    continue
            elif command == "frequency":
                letter_count = {}
                for key in dictionary.keys(): letter_count[key] = 0
                for line in codelines:
                    for char in line: 
                        if char in letter_count.keys(): letter_count[char] += 1
                letter_count_tuple = [(k, v) for k, v in letter_count.items()]
                letter_count_tuple.sort(key = lambda x: -x[1])

                print()
                count = 0
                for k, v in letter_count_tuple:
                    print("{}: {}".format(k, v), end = '\t')
                    count += 1
                    if count == 6: 
                        print()
                        count = 0
                command = ""
                print("\n")
                continue
            elif command == "summary":
                print()
                count = 0
                for key in dictionary.keys():
                    print("{}: {}".format(key, dictionary[key]), end = '\t')
                    count += 1
                    if count == 6: 
                        print()
                        count = 0
                print("\n")
                command = ""
                continue
            elif command == "save":
                savefile = open(args.inputfile + '.p', 'wb')
                pickle.dump(dictionary, savefile)
                savefile.close()
                print("Saved to {}.p".format(args.inputfile))
                command = ""
            elif command == "load":
                try:
                    savefile = open(args.inputfile + '.p', 'rb')
                    dictionary = pickle.load(savefile)
                    savefile.close()
                except Exception as e:
                    print("Error: " + str(e))
                    command = ""
            else:
                print("Command unknown.")
                print("Commands: \n" + commandlist)
                command = ""
                continue
        except KeyboardInterrupt:
            print()
            print("Type quit or exit to exit.")
            command = ""
            continue