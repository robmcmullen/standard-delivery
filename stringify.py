#!/usr/bin/env python
import sys

for name in sys.argv[1:]:
    with open(name, "rb") as fh:
        data = fh.read()
        if data[0:4] == b"\xff\xff\x00\x08":
            print("stripping off atari binary executable header")
            data = data[6:]
        index = data.find("\x34\x12")
        if index > 0:
            print("stripping off $c0 marker and jump target")
            data = data[:index]
        text = repr(data)
        if not text.startswith("b"):
            text = "b" + text

        with open("%s.py" % name, "wb") as w:
            w.write("# generated file - recompile fstbt.s to make changes\n\n# append jump target (lo, hi) and sector address list before saving to disk\n")
            line = "fstbt = %s\n" % (text)
            w.write(line)
