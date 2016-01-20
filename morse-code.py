#!/usr/bin/python

import sys


MORSE_CODE = {'.-...': '&',
                '--..--': ',',
                '....-': '4',
                '.....': '5',
                '...---...': 'SOS',
                '-...': 'B',
                '-..-': 'X',
                '.-.': 'R',
                '.--': 'W',
                '..---': '2',
                '.-': 'A',
                '..': 'I',
                '..-.': 'F',
                '.': 'E',
                '.-..': 'L',
                '...': 'S',
                '..-': 'U',
                '..--..': '?',
                '.----': '1',
                '-.-': 'K',
                '-..': 'D',
                '-....': '6',
                '-...-': '=',
                '---': 'O',
                '.--.': 'P',
                '.-.-.-': '.',
                '--': 'M',
                '-.': 'N',
                '....': 'H',
                '.----.': "'",
                '...-': 'V',
                '--...': '7',
                '-.-.-.': ';',
                '-....-': '-',
                '..--.-': '_',
                '-.--.-': ')',
                '-.-.--': '!',
                '--.': 'G',
                '--.-': 'Q',
                '--..': 'Z',
                '-..-.': '/',
                '.-.-.': '+',
                '-.-.': 'C',
                '---...': ':',
                '-.--': 'Y',
                '-': 'T',
                '.--.-.': '@',
                '...-..-': '$',
                '.---': 'J',
                '-----': '0',
                '----.': '9',
                '.-..-.': '"',
                '-.--.': '(',
                '---..': '8',
                '...--': '3'}


CODE_MAP = {'11': '.',
            '111111': '-',
            '111': '-',
            '000': ' ',
            '1': '.',
            '0': ''}


def decodeBits(bits):
    result = ""
    bits = bits.strip('0')
    for word in bits.split('00000000000000'):
        chars = word.split('000000')
        mword = ""
        for char in chars:
            codes = char.split('00')
            for code in codes:
                try:
                    mword = mword + CODE_MAP[code]
                except KeyError:
                    pass
            mword = mword + " "
        result = result + mword.strip() + "   "
    return result.strip()


def decodeMorse(morseCode):
    words = []
    result = ""
    morseCode = morseCode.strip()
    words = morseCode.split("   ")
    for word in words:
        for w in word.split(' '):
            result = result + MORSE_CODE[w]
        result = result + " "
    return result.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).rstrip()


## print decodeMorse(".... . -.--   .--- ..- -.. .")

print decodeBits(sys.argv[1])
print decodeMorse(decodeBits(sys.argv[1]))


'''

'''
