import re
import time
import datetime
# replace the date
filename = "output_1926.7.26.txt"
m = re.search("output_(\d{4}.\d{1,2}.\d{1,2})", filename)
searchResult = m.group(1)
print "result:" + str(searchResult)
dates = searchResult.split('.')
for date in dates:
    print date
year = dates[0]
month = dates[1]
day = dates[2]
xingqi = datetime.datetime(int(year), int(month), int(day)).strftime("%w")

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "_" + str(xingqi)
new_file = re.sub("\d{4}.\d{1,2}.\d{1,2}", now, filename)
print "new file name:" + new_file
