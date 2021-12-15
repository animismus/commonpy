"""
JF 0.1 08/12/2021 First version
JF 1.0 09/12/2021 Working as intended


DESC
  I had something like this done for ID and I am sure for myself already, but cannot find it.
  redoing it with some options.
  Do not forget that everything is a string when passing args to a script, so no need to add "" to something like //

  -n removes like breaks and replaces them with a space by default or something that the user wants. The sep for exp number is ;
    ex: printit -n ;

  -p saving the procno is ON by default, using this flag does not save it then
    ex: printit -p

  -o if used, the title is appended to the next arg. The file is always saved in the local dataset folder.
     do not try to use full paths
    ex: printit -o outfile.csv



CAVEATS
  - Simple arg parsing with some obvious problems like checking for a possible argument only based on first char (-) 
  - Gave up on exception handling with java.lang.Exception as err
  either way it is better to just let the script crash and give the user a trace stack
"""



import sys
import codecs
import os

ENC = 'cp1252' if System.getProperty("os.name").lower().startswith('win') else 'utf8'
DEFAULT_SEP = ' '

cda = CURDATA()
titlefn = "{3}/{0}/{1}/pdata/{2}/title".format(*cda)
args = list(sys.argv[1:])



def get_tit(fn, enc=ENC):
    fh = codecs.open(fn, "r", encoding=enc)
    dump = fh.read().replace(u"\r", u"")
    fh.close()
    return dump


def append_text(fn, text, enc=ENC):
    fh = codecs.open(fn, "a", encoding=enc)
    fh.write(text +  '\n')
    fh.close()
    return True




def main():
    if not os.path.isfile(titlefn): 
        print "Could not find the title file for this expno/procno"
        titdump = ''
    else: titdump = get_tit(titlefn)


    # -n 
    if '-n' in args:
        possible_sep = args[args.index('-n') + 1]
        sep = possible_sep if not possible_sep.startswith('-') else DEFAULT_SEP
        titdump = titdump.replace('\n', sep) if '-n' in args else titdump

    # -p
    export_str  = cda[1] + ";"
    export_str += "{};".format(cda[2]) if not '-p' in args else ''
    export_str += titdump

    # -o
    if '-o' in args:
        possible_out_fn = args[args.index('-o') + 1]
        outfn = "{}/{}/{}".format(cda[3], cda[0], possible_out_fn)
        print outfn
        append_text(outfn, export_str)
    else:
        print export_str







if __name__ == '__main__':
    main()