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

char2compo = 'Characters2DeepComponents.txt'

f = codecs.open(char2compo, 'r', 'utf-8').readlines()

     	
char2compo = {l.split(':')[0]:[c for c in l.split(':')[1].strip()] for l in f}
maxDiam = max([len(v) for v in char2compo.values()])

nbChar = len(char2compo.keys())
diametersList = []
nbCompo2quantity = {}

refcharvalue = 4


for char, compoList in char2compo.items():
    # if len(compoList) == 1:
    #     continue
    if len(compoList) not in nbCompo2quantity:
        nbCompo2quantity[len(compoList)] = 1 
    else:
        nbCompo2quantity[len(compoList)] += 1
        
    d = {'q':len(compoList), 
        'char':char, 
        'child':[{'q':1, 'char':c} for c in compoList]
        }
    diametersList.append(d)

print(nbCompo2quantity)
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

maxc = max([d['q'] for d in diametersList])

y = H-margins
x = margins
for d in diametersList:
    char = d['char']
    colgreen = d['q']/maxc
    colred = 1-colgreen
    fill(colred, colgreen, 0, 1)
    stroke(None)
    inc = (W-margins*2)/180
    if x > W-margins:
        y -= inc
        x = margins
    size = inc
    drawCircleFromCenter(x, y, size)
    font("BabelStoneHan", size/2)
    save()
    fill(0)
    text(char, (x, y-size/5), align='center')
    restore()
    x += inc

s = W-margins*2
l = s/(maxc+1)
maxq = max([v for k, v in nbCompo2quantity.items()])

for i in range(maxc+1):
    colgreen = i/maxc
    colred = 1-colgreen
    fill(colred, colgreen, 0, 1)
    rect(margins+l*i, margins*2.5, l, margins*.5)
    font("DriveMono-Book", min(H,W)/100)
    fill(1)
    text(str(i+1), (margins+l*i+l/2, margins*3.5), align='center')
    
text('Black[Foundry] Number of deep-components per character (%s characters)' % nbChar, (margins, margins), align='left')
text(month_year, (W-margins, margins), align='right')
 
saveImage('Number-of-Deep-components-per-character.pdf')
saveImage('Number-of-Deep-components-per-character.png')