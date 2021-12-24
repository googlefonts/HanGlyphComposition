
characters_file = "48_basic_Hanzi.txt"
cg2dc_file = "Characters2DeepComponents.txt"
f = open(characters_file).read()
cg2dc = open(cg2dc_file).readlines()
d = {}
for e in cg2dc:

	l = e.split(':')
	c, v = l[0], l[1].strip()
	d[c] = v.split(' ')

s = set()
for e in f:
	print(e, ':', ''.join(d[e]))
	for i in d[e]:
		s.add(i)
print(''.join(s), len(s))