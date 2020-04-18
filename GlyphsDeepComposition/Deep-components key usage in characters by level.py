# coding = utf-8
import datetime
import colorsys

lvl1 = open('../DeepComponents/DeepComponentLevels/Level1.txt', 'r', encoding='utf-8').read()
lvl2 = open('../DeepComponents/DeepComponentLevels/Level2.txt', 'r', encoding='utf-8').read()
lvl3 = open('../DeepComponents/DeepComponentLevels/Level3.txt', 'r', encoding='utf-8').read()
lvl4 = open('../DeepComponents/DeepComponentLevels/Level4.txt', 'r', encoding='utf-8').read()
lvl5 = open('../DeepComponents/DeepComponentLevels/Level5.txt', 'r', encoding='utf-8').read()
lvl6 = open('../DeepComponents/DeepComponentLevels/Level6.txt', 'r', encoding='utf-8').read()

lvls = {lvl1:0, lvl2:1, lvl3:2, lvl4:3, lvl5:4, lvl6:5}

now = datetime.datetime.now()
year = '{:02d}'.format(now.year)
month = '{:02d}'.format(now.month)
month_year = '{}/{}'.format(month, year)

import codecs
import sys
import os
modDir = os.path.expanduser('/usr/local/lib/python3.7/site-packages')
sys.path.append(modDir)

import circlify as circ

compo2char = 'DeepComponents2Characters.txt'

f = codecs.open(compo2char, 'r', 'utf-8').readlines()

     	
compo2char = {l.split(':')[0]:len(l.split(':')[1].strip()) for l in f}
maxDiam = max([k for k in compo2char.values()])



diametersList = {'q':1, 'children':[{'q':0, 'children':[]},
                                    {'q':0, 'children':[]},
                                    {'q':0, 'children':[]},
                                    {'q':0, 'children':[]},
                                    {'q':0, 'children':[]},
                                    {'q':0, 'children':[]}
                                    ]
                }
c = 0
for compo, nbChars in compo2char.items():
#    if c > 100: continue
    for lvl, n in lvls.items():
        if compo in lvl:
            l = int(n)
            break
    diametersList['children'][l]['children'].append({'l':l, 'q':nbChars, 'char':compo})
    diametersList['children'][l]['q'] += nbChars
    c += 1

for e in diametersList['children']:
    e['children'].sort(key=lambda e: e['q'])
    e['children'].reverse()

def drawCircleFromCenter(x, y, diam):
    r = diam / 2
    oval(x-r, y-r, diam, diam)

W = 4000
H = 4000
margins = 100
newPage(W, H)

fill(0, 0, 0, 1)
rect(0, 0, W, H)
fill(1, 0, 0, 1)

circles = circ.circlify([diametersList], id_field='id', datum_field='q', target_enclosure =circ.Circle(0, 0, .95), show_enclosure=False)


for c in circles:
    if not 'char' in c.ex: continue
    char = c.ex['char']
    if char == "":
        fill(None)
    elif not 'children' in c.ex:
        l = c.ex['l']/6
        s = 1-6*(c.ex['q']/maxDiam)
        if char in lvl1:
            color = colorsys.hsv_to_rgb(l, s, 1)
        elif char in lvl2:
            color = colorsys.hsv_to_rgb(l, s, 1)
        elif char in lvl3:
            color = colorsys.hsv_to_rgb(l, s, 1)
        elif char in lvl4:
            color = colorsys.hsv_to_rgb(l, s, 1)
        elif char in lvl5:
            color = colorsys.hsv_to_rgb(l, s, 1)
        elif char in lvl6:
            color = colorsys.hsv_to_rgb(l, s, 1)
        fill(color[0], color[1], color[2], 1)
        
    x, y = W/2+c.x*W*.5, margins*2+H/2+c.y*H*.5
    size = c.r*min(H,W)-7
    drawCircleFromCenter(x, y, size)
    font("BabelStoneHan", size/2)
    fill(0)
    text(char, (x, y-size/5), align='center')

w = width()-margins*2
for i in range(6):
    color = colorsys.hsv_to_rgb(i/6, .8, 1)
    
    # fill(color[0], color[1], color[2], 1)
    
    linearGradient(startPoint=(margins+i*w/6, margins*2.5), endPoint=(margins+i*w/6, margins*3+margins), colors=[(color[0], color[1], color[2]), (1,1,1)])
    
    rect(margins+i*w/6, margins*2.5, w/6, 2*margins)
    
    font("DriveMono-Book", min(H,W)/50)
    fill(0)
    text(str(i+1), (w/12+margins+i*w/6, margins*3.5), align='center')

fill(1)
font("DriveMono-Book", min(H,W)/100)
text('Black[Foundry] Deep-components’ key usage in characters by level (%s keys)' % len(compo2char.keys()), (margins, margins), align='left')
text(month_year, (W-margins, margins), align='right')

saveImage('Deep-components-key-usage-in-characters-by-level.pdf')
saveImage('Deep-components-key-usage-in-characters-by-level.png')