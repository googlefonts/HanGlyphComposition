# coding: utf-8
f = open('Characters2DeepComponents.txt', encoding='utf-8').readlines()
d = {}

for l in f:
	CG, DCs = l.split(':')
	DCs = DCs.strip()
	for DC in DCs:
		if DC not in d:
			d[DC] = set(CG)
		else:
			d[DC].add(CG)

sorted_d = {k: v for k, v in sorted(d.items(), key=lambda item: len(item[1]), reverse=True)}


s = ''
dc = ''
for DC, CGs in sorted_d.items():
	s += ('{}:{}'.format(DC, ''.join(CGs))) + '\n'
	dc += DC
output = open('DeepComponents2characters.txt', 'w', encoding='utf-8')
output.write(s)

onlyDC = open('AllDeepComponents.txt', 'w', encoding='utf-8')
onlyDC.write(dc)