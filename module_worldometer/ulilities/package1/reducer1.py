import sys    

if len(sys.argv) < 2:
    print("Usage: python mapper.py <option>")
    sys.exit(1)

name = sys.argv[1]
for line in sys.stdin:
    data = line.split(",")
    if(data[0]!="\n"):
        a,b = (data[0].strip()),int(data[1].strip())
print(name)
print("query result : " ,a)
print("world %      : ",b)