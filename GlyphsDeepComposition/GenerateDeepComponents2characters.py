from collections import defaultdict
path = '/Users/gaetanbaehr/Documents/BlackFoundry/Tech/Git/HAnGlyphComposition/GlyphsDeepComposition/Characters2DeepComponents.txt'

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
    
output = ""
for i in sorted(list(length.keys()), reverse = True):
    # print(list(length[i]))
    for k in sorted(list(length[i])):
        output += k + ":" + " ".join(sorted(list(dc2char[k]))) + "\n"

outputpath = '/Users/gaetanbaehr/Documents/BlackFoundry/Tech/Git/HAnGlyphComposition/GlyphsDeepComposition/DeepComponents2characters.txt'
with open(outputpath, "w", encoding = "utf-8") as file:
    file.write(output)

# print(dc2char.keys())