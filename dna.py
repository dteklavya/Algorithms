#!/usr/bin/env python

import sys

compl = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}


def DNA_strand(strand):
    return ''.join([compl[i] for i in strand])

print DNA_strand(sys.argv[1])
