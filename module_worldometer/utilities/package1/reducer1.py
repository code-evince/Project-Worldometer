import sys    

# if len(sys.argv) < 2:
#     print("Usage: python mapper.py <option>")
#     sys.exit(1)
options = ['','Total Cases','Active Cases','Total Deaths','Total Recovered','Total Tests','Death/million','Tests/million','New Case','New Death','New Recovered']
name = sys.argv[1]
option = int(sys.argv[2])
for line in sys.stdin:
    data = line.split(",")
    if(data[0]!="\n"):
        a,b = int(data[0].strip()),int(data[1].strip())
print("++++++++++++++++++++++++++++++++++++++++++++++++")
print(name)
print(f"{options[option]}              : " ,a)
print(f"{options[option]} World %      : ",a/b*100,'%')
print("++++++++++++++++++++++++++++++++++++++++++++++++")
print()