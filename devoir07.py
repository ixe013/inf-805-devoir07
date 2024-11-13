#!python3

import base64
import binascii
import re
import sys

import LnkParse3

base64line = re.compile("^[a-zA-Z0-9+/]+(={0,3})?")

def hexdump(data: bytes):
    def to_printable_ascii(byte):
        return chr(byte) if 32 <= byte <= 126 else "."

    offset = 0
    while offset < len(data):
        chunk = data[offset : offset + 16]
        hex_values = " ".join(f"{byte:02x}" for byte in chunk)
        ascii_values = "".join(to_printable_ascii(byte) for byte in chunk)
        print(f"{offset:08x}  {hex_values:<48}  {ascii_values}")
        offset += 16


try:
    # Lire le contenu Base64 depuis stdin
    base64_string = sys.stdin.read()
    # Décoder le contenu
    decoded_bytes = base64.b64decode(base64_string.replace('\n', ''))
    #lnk = LnkParse3.lnk_file(indata)
    lnk = LnkParse3.lnk_file(indata = decoded_bytes)
    target = lnk.print_shortcut_target()


    if not target:
        print("Curated base64:")
        print(base64_string.replace('\n', ''))
        lnk.print_lnk_file()

    hexdump(decoded_bytes)
    print(f"Links to {target}")
    exit(0)
except KeyboardInterrupt:
    exit(1)
