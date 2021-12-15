
"""
JF v1.0 2021-08-25 Working version
JF v1.5 2021-12-15 Working as intended. It was reading old values from procs

DESC
  Go through all the experiments and do a sino calc and then export the value to a file in the dataset root
  sino SIGF1, SIGF2, NOISF1 and NOISF2 noprint

  Was having some trouble running this properly. Looking at curdir/getlim.log it looks like it is 
  ignoring the parameters I pass it in the cli and taking what is saved in proc.


CAVEATS
  - SIGF1/2 and NOISF1/2 are hardcoded in the py file
  - Hardcoded to use only PROCNO 1
  - Slow on purpose to make sure that sino is done before it jumps to another file
"""


import time
import os
import sys
from datetime import datetime as dt

BASE_PROCNO = 1

CDA = CURDATA()


def get_expnos(cda):

    _expnos = os.listdir("{3}/{0}".format(*cda))
    expnos = []
    for ele in _expnos:
        try:
            expnos.append(int(ele))
        except:
            continue

    return sorted(expnos)


def main():
    cda = CURDATA()
    expnos = get_expnos(cda)
    sinosavefn = "{3}/{0}/sinosave.csv".format(*cda)
    args = list(sys.argv[1:])

    # print expnos
    # print len(args), args

    if len(args) < 4: 
        MSG("""Please enter SIGF1, SIGF2, NOISF1 and NOISF2\nEx: sinosave 3 2 13 10""", "Bad arguments")
        return None

    # cmdstrg = 'sino {} {} {} {} noprint'.format(*args)
    # print cmdstrg
    # print CURDATA()
    # XCMD('SIGF1 {}'.format(args[0]))
    # XCMD('SIGF2 {}'.format(args[1]))
    # XCMD('NOISF1 {}'.format(args[2]))
    # XCMD('NOISF2 {}'.format(args[3]))
    # XCMD('sino noprint')
    # print GETPARSTAT('SINO')
    print

    with open(sinosavefn, 'a') as fh:
        cda = CURDATA()
        fh.write('# {}; SIGF1 {}; SIGF2 {}; NOISF1 {}; NOISF2 {}\n'.format(dt.now().strftime('%Y-%m-%d %H:%M:%S'), *args))
        fh.write('# {}/{}\n'.format(cda[-1], cda[0]))

        for expno in expnos:
            # XCMD('re {}'.format(expno))
            # time.sleep(0.25)
            # cda = CURDATA()
            # print cda
            # print cmdstrg
            # print
            # # sino SIGF1, SIGF2, NOISF1 and NOISF2 noprint
            # # XCMD('sino 80 70 380 280 noprint')
            # XCMD(cmdstrg)
            # time.sleep(0.25)
            # fh.write('{};{};{}\n'.format(cda[1], cda[2], GETPARSTAT('S SINO')))
            # time.sleep(0.25)


            XCMD('re {}'.format(expno))
            cda = CURDATA()
            XCMD('SIGF1 {}'.format(args[0]))
            XCMD('SIGF2 {}'.format(args[1]))
            XCMD('NOISF1 {}'.format(args[2]))
            XCMD('NOISF2 {}'.format(args[3]))
            XCMD('sino noprint')
            sinoval = GETPARSTAT('SINO')

            fh.write('{};{};{}\n'.format(cda[1], cda[2], sinoval))
            time.sleep(0.15)


if __name__ == '__main__':
    main()
