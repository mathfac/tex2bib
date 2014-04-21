__author__ = 'mathfac'

import sys
import re

sys.stdin = open("input.txt")
fout = open(sys.argv[2], 'w')
fkeys = open("keys.txt", 'w')

tex = "".join(line for line in sys.stdin)

#print tex

keys = re.findall(r'(\{|\}|\\[a-zA-Z0-9_]+|[a-zA-Z0-9_]+|[ \,\.\:\;\^\$\=\|\-\~\\\>\(\)\*\&]+?)+?', tex, flags=re.MULTILINE)
for key in keys:
    fkeys.write(key + "\n")

res = re.sub(r'(\{|\}|\\[a-zA-Z0-9_]+|[a-zA-Z0-9_]+|[ \,\.\:\;\^\$\=\|\-\~\\\>\(\)\*\&]+?)+?'," , ", tex, count=0, flags=re.MULTILINE)

fout.write(res)
fkeys.close()

fin = open("input2.txt", 'r')
fout = open("output2.txt", 'w')
tex = "".join(line for line in fin.readlines())
texs = re.split(" *\, *",tex)
for (id, block) in enumerate(texs):
    print id, len(texs)
    try:
        fout.write(block + keys[id])
    except: pass
