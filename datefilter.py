import sys
import time
import os
import json
import datetime
import operator

# SELECT * FROM cddata WHERE Date > 2019-01-01 and Date < 2019-01-20
f2 = open('output.txt', 'w')
f2.write('\n')
f2.close()

f2 = open('output.txt', 'a')
for root, dirs, files in os.walk('data'):
    # print(root,dirs,files)
    path = root.split(os.sep)
    for fn in files:
        fp = root+os.sep+fn
        print(fp)
        f = open(fp, 'r')
        for line in f:
            data = json.loads(line)
            payload = data['payload']
            payload = json.loads(payload)
#            print(payload['received'])
            k = payload['received'].split('T')[0]
            if k >= '2019-01-01' and k <= '2019-01-02':
                f2.write(line + '\n')


f2.close()
