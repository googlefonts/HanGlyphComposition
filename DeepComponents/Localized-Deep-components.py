# coding = utf-8
import datetime
import colorsys
import itertools
import codecs
import sys
import os
modDir = os.path.expanduser('/usr/local/lib/python3.7/site-packages')
sys.path.append(modDir)

import circlify as circ

now = datetime.datetime.now()
year = '{:02d}'.format(now.year)
month = '{:02d}'.format(now.month)
month_year = '{}/{}'.format(month, year)

compo2char = 'LocalizedDeepComponents2Characters.txt'
f = codecs.open(compo2char, 'r', 'utf-8').readlines()
compo2char = {l.split(': ')[0]:(len(l.split(': ')[1].strip().split(' ')), l.split(': ')[1].strip().split(' ')) for l in f}

maxDiam = max([k for k in compo2char.values()])[0]
print(maxDiam)

H = ['h', 'x']
T = ['t', 'x']
J = ['j', 'x']
K = ['k', 'x']

obj = itertools.product(H, T, J, K, repeat=1)
regionsGroups = {}
for e in list(obj):
    regionsGroups[''.join(sorted(e, key=lambda x:['h', 't', 'j', 'k']))] = []
    

for k, (n, chars) in compo2char.items():
    groupName = k.split('.')[1].split('_')[1].split('*')[0]
    # print(groupName, k, chars)
    regionsGroups[groupName].append((k, n))


diametersDict = {'q':1, 'children':[]}
regionsList = []
for g, dc in regionsGroups.items():
    # print(g, len(dc))
    if len(dc) > 0:
        diametersDict['children'].append({'q':len(dc), 'name':g, 'children':[{'q':n, 'name':_dc, 'region':g} for (_dc, n) in dc] })
        regionsList.append((g, len(dc)))


for e in diametersDict['children']:
    e['children'].sort(key=lambda e: e['q'])
    e['children'].reverse()

circles = circ.circlify([diametersDict], id_field='id', datum_field='q', target_enclosure =circ.Circle(0, 0, .85), show_enclosure=False)

W = 4000
H = 4000
margins = 100
newPage(W, H)

fill(0, 0, 0, 1)
rect(0, 0, W, H)
fill(1, 0, 0, 1)

def drawCircleFromCenter(x, y, diam):
    r = diam / 2
    oval(x-r, y-r, diam, diam)
    
for c in circles:
    if not 'name' in c.ex: continue
    name = c.ex['name']
    if name in regionsGroups:
        fill(None)
    elif not 'children' in c.ex:
        l = list(regionsGroups.keys()).index(c.ex['region'])/(len(regionsGroups.keys()))
        s = 1-6*(c.ex['q']/maxDiam)
        color = colorsys.hsv_to_rgb(l, s, 1)
        fill(color[0], color[1], color[2], 1)
        
    x, y = W/2+c.x*W*.5, margins*3.5+H/2+c.y*H*.5
    size = c.r*min(H,W)-7
    drawCircleFromCenter(x, y, size)
    font("BabelStoneHan", size/2)
    fill(0)
    text(name.split('.')[0], (x, y-size/5), align='center')

w = width()-margins*2
nbGroups = len(regionsList)

for i, (regionName, number) in enumerate(regionsList):
    color = colorsys.hsv_to_rgb(i/nbGroups, .8, 1)
    regionName = ''.join([c for c in regionName if c != 'x']).upper()
    linearGradient(startPoint=(margins+i*w/nbGroups, margins*2.5), endPoint=(margins+i*w/nbGroups, margins*4+margins), colors=[(color[0], color[1], color[2]), (1,1,1)])
    
    rect(margins+i*w/nbGroups, margins*2.5, w/nbGroups, 3*margins)
    
    font("DriveMono-Book", min(H,W)/50)
    fill(0)
    text(regionName+'\n'+str(number), (w/(nbGroups*2)+margins+i*w/nbGroups, margins*4.5), align='center')

fill(1)
font("DriveMono-Book", min(H,W)/100)
text('Black[Foundry] Localized deep-components’ key usage in characters by region (%s localized keys)' % len(compo2char.keys()), (margins, margins), align='left')
text(month_year, (W-margins, margins), align='right')

saveImage('../DeepComponents/Localized-Deep-components-key-usage-in-characters-by-region.pdf')
saveImage('../DeepComponents/Localized-Deep-components-key-usage-in-characters-by-region.png')