#!python3

import base64
import sys

import LnkParse3

# Lire le contenu Base64 depuis stdin
base64_string = sys.stdin.read()

# Décoder le contenu
decoded_bytes = base64.b64decode(base64_string.replace('\n', ''))
#print(decoded_bytes)

#exit()

#indata = ''.join([line.strip() for line in sys.stdin.readlines()])

#lnk = LnkParse3.lnk_file(indata)
lnk = LnkParse3.lnk_file(indata = decoded_bytes)
lnk.print_shortcut_target()
