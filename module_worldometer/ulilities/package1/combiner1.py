import sys    

if len(sys.argv) < 2:
    print("Usage: python mapper.py <option>")
    sys.exit(1)

name = sys.argv[1]
for line in sys.stdin:
    data = line.split(",")
    sum=0
    # print(line)
    if(data[0]!="\n"):
        a,b = (data[0].strip()),int(data[1].strip())
        sum= sum + b 
        if(a==name):
            country_attrib = b 
print(country_attrib,sum)