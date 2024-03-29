import sys  
import time
SLEEP_TIME = 5 #sleeptime in seconds

if len(sys.argv) < 5:
    print("Usage: python3 <combiner.py path> <start_date> <end_date> <country> <given_country>")
    sys.exit(1)

start_date = sys.argv[1]
end_date = sys.argv[2]
curr_country = sys.argv[3]
given_country = sys.argv[4]
old_cases = 0
new_cases = 0

for line in sys.stdin:
    if(line==""):
        break
    line = line.strip()
    # print(line)
    date, count = line.split("\t")
    date = date[:-1]
    if count == "null":
        count = 0
    if start_date == date:
        old_cases = int(count)
    elif end_date == date:
        new_cases = int(count)
        break

given_country_diff = -1
if curr_country == given_country:
    diff = new_cases - old_cases
    given_country_diff = diff
else:
    time.sleep(SLEEP_TIME)
print(f"{curr_country},{str(new_cases)},{str(old_cases)},{str(given_country_diff)}")

# python3 utilities/package2/mapper2.py cache/country/France.txt 1 start_date end_date country given_country | python3 utilities/package2/combiner2.py 'Apr 08, 2020 ' 'Apr 12, 2020 ' country given_country
  