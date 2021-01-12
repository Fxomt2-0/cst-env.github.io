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
