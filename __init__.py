""" custom env language.

# cstenv.py
cstenv means: custom env lang.

## loading a file
```python
cstenv.load_file(NAME)
```

## defining variables
```
let $varname$ = "hello world!"
let $int$ = 1
```
## loading variables values
```python
cstenv.var["YOURVARNAMEHERE *with no dollar signs.*"]
```
"""

import re

tokens = []
var = {}


def lex(data):
    data = list(data)
    token = ""

    for char in data:
        token += char

        if token == " ":
            token = ""

        elif token == "\n":
            token = ""

        elif token == "let":
            tokens.append("LET")
            token = ""

        elif re.match(r"\$[a-zA-Z0-9_]*\$", token):
            tokens.append("NAME:"+token)
            token = ""

        elif re.match(r"\".*\"", token):
            tokens.append("STR:EXPR:"+token)
            token = ""

        elif re.match(r"\d+", token):
            tokens.append("INT:EXPR:"+token)
            token = ""

        elif token == "=":
            tokens.append("EQ")
            token = ""

    return tokens


def parse(data):
    i = 0
    while i < len(data):
        if data[i]+data[i+1][0:4]+data[i+2]+data[i+3][4:8] == "LETNAMEEQEXPR":
            var.update({str(data[i+1][5:].replace("$", "")): data[i+3][9:].replace("\"", "")})
            i += 4


def load_file(file):
    data = open(file, "r").read()
    parse(lex(data))
