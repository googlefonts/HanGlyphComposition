from collections import defaultdict
path = 'Characters2DeepComponents.txt'

with open(path, 'r', encoding = 'utf-8') as file:
    f = file.readlines()
    
dc2char = defaultdict(list)
for l in f:
    k, v = l.strip().split(":")
    if ' ' in v:
        v = v.split(" ")
        # print(v)
    elif "." in v:
        v = [v]
    # print(v)
    # v = list(v)
    # print(v)
    for dc in v:
        # print(dc)
        dc2char[dc].append(k)
print(dc2char.keys())
        
length = defaultdict(list)
for k, v in dc2char.items():
    length[len(v)].append(k)
    
dcs = []
output = ""
for i in sorted(list(length.keys()), reverse = True):
    # print(list(length[i]))
    for k in sorted(list(length[i])):
        output += k + ":" + " ".join(sorted(list(dc2char[k]))) + "\n"
        dcs.append(k)

outputpath = 'DeepComponents2characters.txt'
with open(outputpath, "w", encoding = "utf-8") as file:
    file.write(output)
    
outalldc = 'AllDeepComponents.txt'

with open(outalldc, "w", encoding = "utf-8") as file:
    file.write(" ".join(sorted(dcs)))

# print(dc2char.keys())