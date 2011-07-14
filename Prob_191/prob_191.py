#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 191
#
# Prize Strings
#
# A particular school offers cash rewards to children with good
# attendance and punctuality. If they are absent for three consecutive
# days or late on more than one occasion then they forfeit their
# prize.
#
# During an n-day period a trinary string is formed for each child
# consisting of L's (late), O's (on time), and A's (absent).
# 
# Although there are eighty-one trinary strings for a 4-day period
# that can be formed, exactly forty-three strings would lead to a
# prize:
# 
#     OOOO OOOA OOOL OOAO OOAA OOAL OOLO OOLA OAOO OAOA
#     OAOL OAAO OAAL OALO OALA OLOO OLOA OLAO OLAA AOOO
#     AOOA AOOL AOAO AOAA AOAL AOLO AOLA AAOO AAOA AAOL
#     AALO AALA ALOO ALOA ALAO ALAA LOOO LOOA LOAO LOAA
#     LAOO LAOA LAAO
#
# How many "prize" strings exist over a 30-day period?
#
# Solved 08/07/10
# 115 problems solved
# Position #868 on level 3 (previously #900 on level 3)


############################################################
# Rearranging the above prize strings...
#
# 1 string with 0 A's, plus 4 L variations = 1 * (1 + 4) = 5
#     OOOO OOOL OOLO OLOO LOOO
#
# 4 strings with 1 A's, each with 3 L variations = 4 * (1 + 3) = 16
#  OOOA OOLA OLOA LOOA
#  OOAO OOAL OLAO LOAO
#  OAOO OAOL OALO LAOO
#  AOOO AOOL AOLO ALOO
#
# 6 strings with 2 A's, each with 2 L variations = 6 * (1 + 2) = 18
#  OOAA OLAA LOAA
#  OAOA OALA LAOA
#  OAAO OAAL LAAO
#  AOOA AOLA ALOA
#  AOAO AOAL ALAO
#  AAOO AAOL AALO
#
# 2 strings with 3 A's, each with 1 L variations = 2 * (1 + 1) = 4
#  AOAA AALA
#  AAOA ALAA
# 


DEPTH = 30

answer = 0
attend = ['O']*DEPTH
alen = 0
ocnt = 0

def down(attend, alen, ocnt):
    global answer
    # Reached full recursion depth, count answers
    if (alen == DEPTH):
        answer += ocnt+1
        # print ">", attend, ocnt+1, alen
        return

    # Recurse with an 'O'
    attend[alen] = 'O'
    alen += 1
    ocnt += 1
    down(attend, alen, ocnt)
    alen -= 1
    ocnt -= 1

    # Recurse with an 'A' only if one of the previous two days were O's
    if ((alen <= 1) | (attend[alen-1] == 'O') | (attend[alen-2] == 'O')):
        attend[alen] = 'A'
        # print attend, ocnt+1, alen, attend[alen], attend[alen-1]
        alen += 1
        down(attend, alen, ocnt)
        alen -= 1

down(attend, alen, ocnt)
print "For strings of length", DEPTH, "the answer is", answer
