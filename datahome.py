import sys
import time
import os
import json
import datetime
import operator
# SELECT temp_5, temp_8 FROM print_reading WHERE pitime > 2018-05-06 16:00:00 AND pitime < 2018-05-06 18:00:00;
# SELECT AVG(temp_8) FROM print_reading WHERE pitime > 2018-05-05 16:00:00 AND pitime < 2018-05-07 16:00:00;f2 = open('output.txt', 'w')

f2.write('\n')
f2.close()
f2 = open('output.txt', 'a')

for root, dirs, files in os.walk('datahome'):
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
