#!/usr/bin/env python
'''

'''

import sys


def cat_digits(digits):
    number = 0
    for index, digit in enumerate(digits):
        number = number + (digit * (10 ** index))
    return number


def next_bigger(number):
    digits = []
    tail = 1
    while(number > 0):
        number, tail = divmod(number, 10)
        digits.append(tail)
    for index, digit in enumerate(digits):
        for i in range(index + 1, len(digits)):
            if digit > digits[i]:
                if next_bigger(cat_digits(digits[index:i])) == -1:
                    digits[index], digits[i] = digits[i], digits[index]
                    digits[0:i] = reversed(digits[0:i])
                    return cat_digits(digits)
                else:
                    continue
    return -1

print next_bigger(int(sys.argv[1]))

'''

# 59884848459853 returns 59884848559834 should equal 59884848483559


TEST CASES FROM CODEWARS

Basic tests
Small numbers
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Bigger numbers
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Random tests
Testing for 11929954270340
Test Passed
Testing for 5995
Test Passed
Testing for 86654322111
Test Passed
Testing for 158113
Test Passed
Testing for 99
Test Passed
Testing for 6598260637
Test Passed
Testing for 9094050661384
Test Passed
Testing for 10257
Test Passed
Testing for 4678468457
Test Passed
Testing for 32
Test Passed
Testing for 21640507
Test Passed
Testing for 80715180872668
Test Passed
Testing for 82654014662
Test Passed
Testing for 200
Test Passed
Testing for 987655443330
Test Passed
Testing for 7
Test Passed
Testing for 75194039047
Test Passed
Testing for 3
Test Passed
Testing for 344487
Test Passed
Testing for 718512
Test Passed
Testing for 44
Test Passed
Testing for 30887080
Test Passed
Testing for 2189874
Test Passed
Testing for 987665421
Test Passed
Testing for 10
Test Passed
Testing for 2
Test Passed
Testing for 43000723877
Test Passed
Testing for 5878429262
Test Passed
Testing for 91887919180
Test Passed
Testing for 977531
Test Passed
Testing for 94220
Test Passed
Testing for 80041
Test Passed
Testing for 688432
Test Passed
Testing for 84
Test Passed
Testing for 93132947901551
Test Passed
Testing for 1
Test Passed
Testing for 82
Test Passed
Testing for 20251265752
Test Passed
Testing for 29
Test Passed
Testing for 967
Test Passed
Testing for 3
Test Passed
Testing for 1661257
Test Passed
Testing for 3718828892
Test Passed
Testing for 520321904661
Test Passed
Testing for 848777215270
Test Passed
Testing for 506623858720
Test Passed
Testing for 36368
Test Passed
Testing for 75915134460
Test Passed
Testing for 473417496
Test Passed
Testing for 469401901
Test Passed
Testing for 58180
Test Passed
Testing for 57767125110853
Test Passed
Testing for 3129262881
Test Passed
Testing for 5
Test Passed
Testing for 88288207
Test Passed
Testing for 5732
Test Passed
Testing for 33624071
Test Passed
Testing for 93
Test Passed
Testing for 658
Test Passed
Testing for 651504816643
Test Passed
Testing for 34898306842761
Test Passed
Testing for 142801
Test Passed
Testing for 9449
Test Passed
Testing for 32347312165078
Test Passed
Testing for 556857853590
Test Passed
Testing for 81
Test Passed
Testing for 88876654221100
Test Passed
Testing for 373491568192
Test Passed
Testing for 584450
Test Passed
Testing for 2
Test Passed
Testing for 92
Test Passed
Testing for 98
Test Passed
Testing for 89278525780858
Test Passed
Testing for 64814
Test Passed
Testing for 3
Test Passed
Testing for 7637
Test Passed
Testing for 95879221837218
Test Passed
Testing for 86651521735
Test Passed
Testing for 42552
Test Passed
Testing for 94954724603365
Test Passed
Testing for 383
Test Passed
Testing for 302588058
Test Passed
Testing for 313395
Test Passed
Testing for 1
Test Passed
Testing for 895323103024
Test Passed
Testing for 6
Test Passed
Testing for 37754614208
Test Passed
Testing for 99951716039813
Test Passed
Testing for 133130
Test Passed
Testing for 427363990
Test Passed
Testing for 4856873403
Test Passed
Testing for 76
Test Passed
Testing for 190906132
Test Passed
Testing for 22015238
Test Passed
Testing for 57012
Test Passed
Testing for 939679
Test Passed
Testing for 3400459
Test Passed
Testing for 37180598
Test Passed
Testing for 27537
Test Passed
Testing for 2666719555525
Test Passed
Testing for 9830220093209
Test Passed
Testing for 37
Test Passed
Testing for 1989
Test Passed
Testing for 84521886
Test Passed
Testing for 9876655322110
Test Passed
Testing for 58
Test Passed
Testing for 385102358682
Test Passed
Testing for 8058
Test Passed
Testing for 511359
Test Passed
Testing for 3
Test Passed
Testing for 6896722976688
Test Passed
Testing for 7772
Test Passed
Testing for 792611
Test Passed
Testing for 12396
Test Passed
Testing for 4708
Test Passed
Testing for 84499688193364
Test Passed
Testing for 49095515
Test Passed
Testing for 66346071
Test Passed
Testing for 73
Test Passed
Testing for 25297
Test Passed
Testing for 45442855
Test Passed
Testing for 5363438
Test Passed
Testing for 1
Test Passed
Testing for 8978562112
Test Passed
Testing for 38208525697
Test Passed
Testing for 346
Test Passed
Testing for 26223576
Test Passed
Testing for 2453691484060
Test Passed
Testing for 3
Test Passed
Testing for 12339960471
Test Passed
Testing for 85675737589
Test Passed
Testing for 54
Test Passed
Testing for 3493500253
Test Passed
Testing for 882881
Test Passed
Testing for 435
Test Passed
Testing for 82651
Test Passed
Testing for 15376024
Test Passed
Testing for 5739808606904
Test Passed
Testing for 5
Test Passed
Testing for 98888654433200
Test Passed
150 Passed
0 Failed
0 Errors

Process took 178ms to complete


'''
