#!/usr/bin/env python3

import sys
from kanji_to_romaji.kanji_to_romaji_module import kanji_to_romaji

if __name__ == "__main__":
    print(kanji_to_romaji(("".join(sys.argv[1:]))))
