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
partitiondir = "partitioned/"
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
            # 2018-02-26T14:28:48.096377
            # print(partfn)
            # Opening a new file in partitioned dir
            fout = open(partitiondir + partfn + '.txt', 'a')
            fout.write(line + '\n')
            fout.write(json.dumps(payload) + '\n')
            fout.close()

        f.close()
