import re
frase = '"on", "50", "16777215" "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"'
re.findall(r"(?:'.*?')|(?:\".*?\")", frase)