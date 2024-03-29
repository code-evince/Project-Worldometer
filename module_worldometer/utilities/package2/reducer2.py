import sys    

if len(sys.argv) < 5:
    print("Usage: python3 <reducer.py path> <option> <start_date> <end_date> <given_country>")
    sys.exit(1)

options = ("Change in active cases","Change in daily death","Change in new recovered","Change in new cases")
option = int(sys.argv[1])
start_date = sys.argv[2]
end_date = sys.argv[3]
given_country = sys.argv[4]
temp_num = temp_den = 0
close = ""
centre = ""
closest = sys.maxsize
close_stat = 0
flag = True

for line in sys.stdin:
    if(line==""):
        break
    line = line.strip()
    # print(line,'#')
    if flag:
        country, newstat, oldstat, centre = line.split(",")
        flag = False
    else:
        country, newstat, oldstat, inp = line.split(",")
    newstat = int(newstat)
    oldstat = int(oldstat)
    diff = newstat - oldstat
    if country == given_country:
        temp_num = diff
        temp_den = oldstat
    else:
        #centre is given_country's change in cases
        centre = int(centre)
        x = abs(centre - diff)
        if closest > x:
            closest = x
            close_stat = diff
            close = country

# Output
print("++++++++++++++++++++++++++++++++++++++++++++++++")
print(f"         -::{given_country} Stats::-")
print(f"{options[option-1]}      : {temp_num}")
if temp_num<0:
    temp_num = abs(temp_num)
    flow = "Decresed"
else:
    flow = "Increased"
print(f"                         : {temp_num} cases {flow}")
if temp_den == 0:
    percentage = 0
else:
    percentage = (temp_num/temp_den)*100
print(f"{options[option-1]} in % : {flow} {percentage}%")
print(f"Closest country : {close} with {close_stat} cases!!")
print("++++++++++++++++++++++++++++++++++++++++++++++++")
print()


# # (python3 utilities/package2/mapper2.py cache/country/France.txt 1 start_date end_date France France | python3 utilities/package2/combiner2.py 'Apr 08, 2020 ' 'Apr 12, 2020 ' France France & python3 utilities/package2/mapper2.py cache/country/India.txt 1 start_date end_date India France | python3 utilities/package2/combiner2.py 'Apr 08, 2020 ' 'Apr 12, 2020 ' India France & python3 utilities/package2/mapper2.py cache/country/USA.txt 1 start_date end_date USA France) | python3 utilities/package2/combiner2.py 'Apr 08, 2020 ' 'Apr 12, 2020 ' USA France | python3 utilities/package2/reducer2.py 1 'Apr 08, 2020 ' 'Apr 12, 2020 ' France 
