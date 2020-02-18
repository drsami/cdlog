import sys
import time
import os
import json
import operator
import datetime
import time

# SELECT * FROM cddata WHERE Date > 2019-01-01 and Date < 2019-01-20
# append all json strings to new file called output.txt
dateCount = {}
start_date = datetime.datetime(2019, 1, 1).date()
end_date = datetime.datetime(2019, 1, 20).date()

myfile = open('output.txt', 'w')
myfile.write('')
myfile.close()
myfile = open('output.txt', 'a')
dtdur = 0
fwdur = 0
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

            # print(payload['received'])
            k = payload['received'].split('T')[0]
            start = time.time()
            date_obj = datetime.datetime.strptime(k, '%Y-%m-%d').date()
            end = time.time()
            dur = end - start
            dtdur += dur
            # print(type(date_obj))
            # print(date_obj)
            start = time.time()
            if(date_obj > start_date and date_obj < end_date):
                myfile.write(line)
                # print(date_obj)
            end = time.time()
            dur = end - start
            fwdur += dur
            # print(k)


myfile.close()
print(dtdur, fwdur)
# 0 == key , 1 == value

# print(sorted_dc)
