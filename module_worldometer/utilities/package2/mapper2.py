import sys  

if len(sys.argv) < 7:
    print("Usage: python3 <mapper.py path> <country.txt> <option> <start_date> <end_date> <country> <given_country>")
    sys.exit(1)

col = int(sys.argv[2])
# print(col)

ipfile = sys.argv[1]
# print(ipfile)
with open(ipfile,'r') as f:
    for line in f:
        if(line==""):
            break
        line = line.strip()
        row = line.split("\t")
        print(row[0],"\t",row[col])
        
# python3 utilities/package2/mapper2.py cache/country/France.txt 1 start_date end_date country given_country
        