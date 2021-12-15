# JF v1.0 2021-08-25
"""
sino SIGF1, SIGF2, NOISF1 and NOISF2 noprint
"""


import time
import os

BASE_PROCNO = 1

cda = CURDATA()
sinosavefn = "{3}/{0}/sinosave.csv".format(*cda)

def get_expnos(cda):

    _expnos = os.listdir("{3}/{0}".format(*cda))
    expnos = []
    for ele in _expnos:
        try:
            expnos.append(int(ele))
        except:
            continue

    return sorted(expnos)


expnos = get_expnos(cda)
print expnos


with open(sinosavefn, 'a') as fh:
    for expno in expnos:
        XCMD('re {}'.format(expno))
        time.sleep(0.25)
        cda = CURDATA()
        # sino SIGF1, SIGF2, NOISF1 and NOISF2 noprint
        # XCMD('sino 80 70 380 280 noprint')
        XCMD('sino 2.9 2.4786 13 9 noprint')
        time.sleep(0.25)
        fh.write('{};{};{}\n'.format(cda[1], cda[2], GETPARSTAT('SINO')))
        time.sleep(0.25)