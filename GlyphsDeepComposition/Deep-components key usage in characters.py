# coding = utf-8
import datetime

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



diametersList = []
c = 0
for compo, nbChars in compo2char.items():
#    if c > 100: continue
    diametersList.append({'q':nbChars, 'char':compo})
    c += 1

diametersList.sort(key=lambda e: e['q'])
diametersList.reverse()

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

diametersList = diametersList
circles = circ.circlify(diametersList, id_field='id', datum_field='q', target_enclosure=circ.Circle(0, 0, .8), show_enclosure=False)

maxc = max([c.r for c in circles])
divide = 2
divideMore = 8
for c in circles:
    char = c.ex['char']
    if char == "":
        fill(None)
    elif not 'children' in c.ex:
        colred = (maxDiam-c.ex['q'])/maxDiam
        colgreen = c.ex['q']/(maxDiam/divideMore)
        colblue = ((maxDiam-c.ex['q'])/maxDiam)/divide
        
        fill(colred, colgreen, colblue, 1)
        
    x, y = W/2+c.x*W*.5, margins*2+H/2+c.y*H*.5
    size = c.r*min(H,W)-7
    drawCircleFromCenter(x, y, size)
    font("BabelStoneHan", size/2)
    fill(0)
    text(char, (x, y-size/5), align='center')

s = W-margins*2
for i in range(s):
    colred = (s-i)/maxDiam
    colgreen = i/(maxDiam/divideMore)
    colblue = ((s-i)/maxDiam)/divide
    
    fill(colred, colgreen, colblue, 1)
    rect(margins+1*i, margins*2.5, 2, margins*.5)


font("DriveMono-Book", min(H,W)/100)
fill(1)
text("1", (margins, margins*3.5), align='left')
text(str(int(maxDiam/15)), (W/15, margins*3.5), align='center')
text(str(int(maxDiam/6)), (W/6, margins*3.5), align='center')
text(str(int(maxDiam/3)), (W/3, margins*3.5), align='center')
text(str(int(maxDiam/1.5)), (W/1.5, margins*3.5), align='center')
text(str(maxDiam), (W-margins, margins*3.5), align='right')
text('Black[Foundry] Deep-components’ key usage in characters (%s keys)' % len(compo2char.keys()), (margins, margins), align='left')
text(month_year, (W-margins, margins), align='right')

saveImage('Deep-components-key-usage-in-characters.pdf')
saveImage('Deep-components-key-usage-in-characters.png')