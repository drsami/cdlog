import sys
import time
import os
import json
import operator
import datetime
import time

# SELECT * FROM cddata WHERE Date > 2019-01-01 and Date < 2019-01-20
# append all json strings to new file called output.txt
# Backslash at the end of the dir but os.sep will be much better option
buf = ''
n = 0
lastpartfn = ''
partitiondir = "partitioned1/"
for root, dirs, files in os.walk('data'):
    path = root.split(os.sep)
    for fn in files:
        fp = root+os.sep+fn
        print(fp)
        f = open(fp, 'r')
        for line in f:
            data = json.loads(line)
            payload = data['payload']
            payload = json.loads(payload)
            partfn = payload['received'].split('T')[0].replace('-', '_')

            buf += json.dumps(payload) + '\n'
            if n % 500 == 0 or partfn != lastpartfn:
                fout = open(partitiondir + partfn + '.txt', 'a')
                fout.write(buf)
                fout.close()
                buf = ''
            n += 1
            lastpartfn = partfn
        fout.write(buf)
        fout.close()
        buf = ''
        f.close()
