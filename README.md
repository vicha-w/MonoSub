# MonoSub
Simple CLI to help decipher monoalphabetic ciphers

## Usage
`python3 MonoSub.py <text file to decipher>`

## Features
- Simple UI showing text and deciphered text.
- Count character frequencies.
- Save your solution and load them later.

## Commands
- `add <source> <dest>` adds transformation rule from each character in `source` to each character in `dest`. For example, `add abc the` changes `a` to `t`, `b` to `h`, and `c` to `e`.
- `remove <char>` resets one character at a time.
- `clear` resets all characters.
- `frequency` shows the frequency of all characters.
- `autofreq (on/off)` turns auto printing of character frequency on or off.
- `summary` summarises all transformation rules.
- `save` saves transformation rules into a pickle file.
- `load` loads transformation rules from a pickle file made by `save` command.
- `quit` or `exit` quits. Much easier than `vim`.