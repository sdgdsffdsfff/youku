#!/usr/bin/env python
# encoding: utf-8

import sys,os
try:
    rfile = sys.argv[1]
except:
    os.system("python sendmail.py")
wfile = rfile[:-4].replace('log','express_log') +"-express.log"
print wfile
#time = rfile[0:12]
f = open(rfile)
c = f.readlines()

out = open(wfile,'w')

for line in c:
    try:
        parts = line.split('^')
        part=parts[8].split('|')
        out.write(parts[3] + '\t'
            + parts[4] + '\t'
            + parts[42] + '\t'
            + parts[43] + '\t'
            + '' + '\t'
            + parts[6] + '\t'
            + parts[24] + '\t'
            + parts[44] + '\t'
            + parts[45] + '\t'
            + parts[46] + '\t'
            + part[0]+'|'+part[1] + '\t'
            + parts[2] + '\t'
            + parts[47])
    except Exception,e:
        print e
f.close()
out.close()
